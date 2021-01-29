"""Interface into collection containing span information."""
import base64
from enum import Enum
from typing import Any, Dict, Generator, List, Optional, Set

from google.protobuf.duration_pb2 import Duration
from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.timestamp_pb2 import Timestamp
from pymongo import DESCENDING
from pymongo.database import Database

from jaeger_grpc_server.db.collection import Collection
from jaeger_grpc_server.generated.model_pb2 import DependencyLink, Span, SpanRef
from jaeger_grpc_server.generated.storage_pb2 import Operation, TraceQueryParameters

SPAN_COLLECTION_NAME = "spans"
SPAN_KIND_NAME = "span.kind"


class RefType(Enum):
    """Possible different span reference types."""

    CHILD_OF = 0
    FOLLOWS_FROM = 1


class SpanCollection(Collection):
    """Pointer to the span collection."""

    def __init__(self, db: Database) -> None:
        """Create a pointer to the span collection."""
        super().__init__(db, SPAN_COLLECTION_NAME)

    def create_indexes(self) -> None:
        """Create indexes required for the given collection."""
        pass

    def add_span(self, span: Span) -> None:
        """
        Add a span to the database.

        :param span: The Span instance to add.
        """
        self.collection.insert_one(self.make_span_dict(span))

    def find_trace(self, trace_id: bytes) -> Generator[Span, None, None]:
        """
        Find the trace with the given id.

        :param trace_id: The id of the trace to find.
        :return: A generator yielding all the spans in the trace.
        """
        results = self.collection.find({"traceId": self.make_trace_id(trace_id)})
        for result in results:
            yield self.make_span_from_db(result)

    def find_services(self) -> List[str]:
        """
        Find all the services that are being tracked.

        :return: A list of the names of all the known services.
        """
        results = self.collection.distinct("process.serviceName")
        return [result for result in results]

    def find_operations(self, span_kind: str, service: str) -> List[Operation]:
        """
        Find all the operations for the given service of the given kind.

        :param span_kind: What kind of span the operation needs to have been done.
        :param service: What service to find the operations for.
        :return: A list of all the Operations that match the given input.
        """
        match_query = [{"process.serviceName": service}]
        if span_kind != "":
            tag_query = {"tags": {"$elemMatch": {"key": SPAN_KIND_NAME, "vStr": span_kind}}}
            match_query.append(tag_query)
        match_stage = {"$and": match_query}
        aggregation = [
            {"$match": match_stage},
            {"$unwind": {"path": "$tags"}},
            {"$match": {"tags.key": "span.kind"}},
            {"$group": {"_id": {"operationName": "$operationName", "tags": "$tags"}}},
            {"$replaceRoot": {"newRoot": "$_id"}},
        ]
        results = self.collection.aggregate(aggregation)
        return [
            Operation(name=result["operationName"], span_kind=result["tags"]["vStr"])
            for result in results
        ]

    def find_traces(self, params: TraceQueryParameters) -> Generator[Span, None, None]:
        """
        Find all the traces that match the given parameters.

        :param params: The given search parameters.
        :return: A generator that yields spans that belong to the matched traces.
        """
        query = self._create_query_from_trace_params(params)
        results = (
            self.collection.find(query).limit(params.num_traces).sort("start_time", DESCENDING)
        )
        for result in results:
            yield self.make_span_from_db(result)

    def find_trace_ids(self, params: TraceQueryParameters) -> Set[bytes]:
        """
        Find the ids of the traces that match the given parameters.

        :param params: The given search parameters.
        :return: A list of all the ids of the matched traces.
        """
        query = self._create_query_from_trace_params(params)
        results = (
            self.collection.find(query).limit(params.num_traces).sort("start_time", DESCENDING)
        )
        return {self.make_span_from_db(span).trace_id for span in results}

    def find_dependencies(
        self, start_time: Optional[Timestamp], end_time: Optional[Timestamp]
    ) -> List[DependencyLink]:
        """
        Find the dependencies between services.

        :param start_time: The time after which a span must have been created to be considered.
        :param end_time: The time before which a span must have been created to be considered.
        :return: A list of all the dependencies found in the matched spans.
        """
        query = []
        if start_time:
            query.append({"startTime": {"$gt": start_time.ToDatetime()}})
        if end_time:
            query.append({"startTime": {"$lt": end_time.ToDatetime()}})
        trace_ids = self.collection.distinct("traceId", {"$and": query})
        dep_maps: Dict[str, DependencyLink] = {}
        for trace_id in trace_ids:
            spans = [
                self.make_span_from_db(cur) for cur in self.collection.find({"traceId": trace_id})
            ]
            for span in spans:
                parent_span: Optional[Span] = next(
                    (cur for cur in spans if cur.span_id == self._find_parent_span_id(span)), None
                )
                if parent_span:
                    parent_service_name = parent_span.process.service_name
                    cur_span_service_name = span.process.service_name
                    if parent_service_name == cur_span_service_name:
                        continue
                    dep_key = parent_service_name + "&&&" + cur_span_service_name
                    dep = dep_maps.get(dep_key)
                    if dep:
                        dep.call_count += 1
                    else:
                        dep_maps[dep_key] = DependencyLink(
                            parent=parent_service_name, child=cur_span_service_name, call_count=1
                        )
        return [value for value in dep_maps.values()]

    @staticmethod
    def make_span_dict(span: Span) -> Dict:
        """
        Turn a Span into something that can be stored in MongoDB.

        :param span: The span to convert.
        :return: A dictionary representation of the given Span.
        """
        res = MessageToDict(span)
        res["startTime"] = span.start_time.ToDatetime()
        res["duration"] = span.duration.ToMicroseconds()
        return res

    @staticmethod
    def make_span_from_db(ret: Dict) -> Span:
        """
        Create a Span object from a Dict that came from MongoDB.

        :param ret: The Dict that came from MongoDB.
        :return: The Span object created from the given Dict.
        """
        duration = Duration()
        duration.FromMicroseconds(ret["duration"])
        start_time = Timestamp()
        start_time.FromDatetime(ret["startTime"])
        del ret["startTime"]
        del ret["duration"]
        span = ParseDict(
            ret, Span(duration=duration, start_time=start_time), ignore_unknown_fields=True
        )
        return span

    @staticmethod
    def make_trace_id(trace_id: bytes) -> str:
        """
        Turn the bytes that represent a trace_id into a string.

        This conversion mimics how MessageToDict from the protobuf library converts bytes into
        strings.

        :param trace_id: The trace_id to convert into a string.
        :return: The string representation of the given trace_id.
        """
        return base64.b64encode(trace_id).decode("utf-8")

    @staticmethod
    def _find_parent_span_id(span: Span) -> bytes:
        """
        Find the span_id of the parent of the given Span.

        If no parent can be found for the given Span, that means it is the first span in the trace.

        :param span: The span to find the parent of.
        :return: The span_id of the parent of the given span, if one exists. bytes(0) otherwise.
        """
        for ref in span.references:
            ref: SpanRef = ref
            if ref.trace_id == span.trace_id and ref.ref_type == RefType.CHILD_OF.value:
                return ref.span_id
        return bytes(0)

    @staticmethod
    def _create_query_from_trace_params(params: TraceQueryParameters) -> Dict[str, Any]:
        """
        Create a MongoDB query from the given TraceQueryParameters.

        :param params: The parameters to convert.
        :return: A Dict representing a MongoDB match query.
        """
        query = []
        if params.service_name:
            query.append({"process.serviceName": params.service_name})
        if params.operation_name:
            query.append({"operationName": params.operation_name})
        if params.duration_min:
            dur_min = params.duration_min.ToMicroseconds()
            if dur_min != 0:
                query.append({"duration": {"$gt": dur_min}})
        if params.duration_max:
            dur_max = params.duration_max.ToMicroseconds()
            if dur_max != 0:
                query.append({"duration": {"$lt": dur_max}})
        if params.start_time_min:
            query.append({"startTime": {"$gt": params.start_time_min.ToDatetime()}})
        if params.start_time_max:
            query.append({"startTime": {"$lt": params.start_time_max.ToDatetime()}})

        for key, value in params.tags.items():
            query.append(SpanCollection._make_generic_tag_match(key, value))

        return {"$and": query}

    @staticmethod
    def _make_generic_tag_match(key: str, value: str) -> Dict[str, Any]:
        """
        Create a query for searching on the tags of spans.

        Currently, these fields are stored as strings in the database. This means our given value
        could match against any one of these fields.

        :param key: The key of the Span Tag to try to match against.
        :param value: The value of the Span Tag to try to match against.
        :return: A mongoDB query.
        """
        query = {
            "tags": {
                "$elemMatch": {
                    "key": key,
                    "$or": [
                        {"vStr": value},
                        {"vInt64": value},
                        {"vBool": value},
                        {"vFloat64": value},
                        {"vBinary": value},
                    ],
                }
            }
        }
        return query
