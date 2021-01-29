"""The span reader grpc service implementation."""
from __future__ import annotations

from typing import Generator

from grpc import ServicerContext

import jaeger_grpc_server.generated.storage_pb2 as storage
from jaeger_grpc_server.db.mongo_client import MongoWrapper
from jaeger_grpc_server.generated.storage_pb2_grpc import SpanReaderPluginServicer


class SpanReaderService(SpanReaderPluginServicer):
    """The SpanReader grpc service implementation."""

    def __init__(self, db: MongoWrapper):
        """
        Create an instance of the SpanReaderService.

        :param db: A MongoWrapper instance.
        """
        self.db = db

    def GetTrace(
        self, request: storage.GetTraceRequest, context: ServicerContext
    ) -> Generator[storage.SpansResponseChunk, None, None]:
        """
        Get a trace given a trace_id.

        :param request: The request with the id of the trace to find.
        :param context: The grpc context of the request.
        :return: A generator yielding spans in a SpansResponseChunk object.
        """
        results = self.db.span_collection.find_trace(request.trace_id)
        for result in results:
            yield storage.SpansResponseChunk(spans=[result])

    def GetServices(
        self, request: storage.GetServicesRequest, context: ServicerContext
    ) -> storage.GetServicesResponse:
        """
        Get the services of the traced spans.

        :param request: A GetServicesRequest instance.
        :param context: The grpc context of the request.
        :return: A GetServicesResponse containing a list of all the known services.
        """
        services = self.db.span_collection.find_services()
        return storage.GetServicesResponse(services=services)

    def GetOperations(
        self, request: storage.GetOperationsRequest, context: ServicerContext
    ) -> storage.GetOperationsResponse:
        """
        Get all the operations that match the given parameters.

        :param request: A request containing a span_kind and a service name.
        :param context: The grpc context of the request.
        :return: A GetOperationsResponse containing a list of the matching operations.
        """
        operations = self.db.span_collection.find_operations(
            span_kind=request.span_kind, service=request.service
        )
        return storage.GetOperationsResponse(operations=operations)

    def FindTraces(
        self, request: storage.FindTracesRequest, context: ServicerContext
    ) -> Generator[storage.SpansResponseChunk, None, None]:
        """
        Find all the traces that match the given parameters.

        :param request: Search parameters to use when finding traces.
        :param context: The grpc context of the request.
        :return: A generator yielding spans in a SpansResponseChunk object.
        """
        spans = self.db.span_collection.find_traces(request.query)
        for span in spans:
            yield storage.SpansResponseChunk(spans=[span])

    def FindTraceIDs(
        self, request: storage.FindTraceIDsRequest, context: ServicerContext
    ) -> storage.FindTraceIDsResponse:
        """
        Find the ids of all the traces that match the given parameters.

        :param request: Search parameters to use when finding traces.
        :param context: The grpc context of the request.
        :return: A FindTraceIDsResponse object that contains a list of all the trace_ids find.
        """
        trace_ids = self.db.span_collection.find_trace_ids(request.query)
        return storage.FindTraceIDsResponse(trace_ids=trace_ids)
