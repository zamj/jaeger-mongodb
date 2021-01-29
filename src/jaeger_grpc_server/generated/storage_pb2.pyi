# @generated by generate_proto_mypy_stubs.py.  Do not edit!
# flake8: noqa
import sys
from typing import Iterable as typing___Iterable
from typing import Mapping as typing___Mapping
from typing import MutableMapping as typing___MutableMapping
from typing import Optional as typing___Optional
from typing import Text as typing___Text

from google.protobuf.descriptor import Descriptor as google___protobuf___descriptor___Descriptor
from google.protobuf.descriptor import (
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.duration_pb2 import Duration as google___protobuf___duration_pb2___Duration
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.internal.containers import (
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.timestamp_pb2 import Timestamp as google___protobuf___timestamp_pb2___Timestamp
from typing_extensions import Literal as typing_extensions___Literal

from jaeger_grpc_server.generated.model_pb2 import DependencyLink as model_pb2___DependencyLink
from jaeger_grpc_server.generated.model_pb2 import Span as model_pb2___Span

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetDependenciesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def start_time(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    @property
    def end_time(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    def __init__(
        self,
        *,
        start_time: typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        end_time: typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "end_time", b"end_time", "start_time", b"start_time"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "end_time", b"end_time", "start_time", b"start_time"
        ],
    ) -> None: ...

type___GetDependenciesRequest = GetDependenciesRequest

class GetDependenciesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def dependencies(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        model_pb2___DependencyLink
    ]: ...
    def __init__(
        self,
        *,
        dependencies: typing___Optional[typing___Iterable[model_pb2___DependencyLink]] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["dependencies", b"dependencies"]
    ) -> None: ...

type___GetDependenciesResponse = GetDependenciesResponse

class WriteSpanRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def span(self) -> model_pb2___Span: ...
    def __init__(
        self,
        *,
        span: typing___Optional[model_pb2___Span] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["span", b"span"]
    ) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal["span", b"span"]) -> None: ...

type___WriteSpanRequest = WriteSpanRequest

class WriteSpanResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(
        self,
    ) -> None: ...

type___WriteSpanResponse = WriteSpanResponse

class GetTraceRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    trace_id: builtin___bytes = ...
    def __init__(
        self,
        *,
        trace_id: typing___Optional[builtin___bytes] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["trace_id", b"trace_id"]
    ) -> None: ...

type___GetTraceRequest = GetTraceRequest

class GetServicesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(
        self,
    ) -> None: ...

type___GetServicesRequest = GetServicesRequest

class GetServicesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    services: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    def __init__(
        self,
        *,
        services: typing___Optional[typing___Iterable[typing___Text]] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["services", b"services"]
    ) -> None: ...

type___GetServicesResponse = GetServicesResponse

class GetOperationsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    service: typing___Text = ...
    span_kind: typing___Text = ...
    def __init__(
        self,
        *,
        service: typing___Optional[typing___Text] = None,
        span_kind: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal["service", b"service", "span_kind", b"span_kind"],
    ) -> None: ...

type___GetOperationsRequest = GetOperationsRequest

class Operation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    name: typing___Text = ...
    span_kind: typing___Text = ...
    def __init__(
        self,
        *,
        name: typing___Optional[typing___Text] = None,
        span_kind: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["name", b"name", "span_kind", b"span_kind"]
    ) -> None: ...

type___Operation = Operation

class GetOperationsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    operationNames: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        typing___Text
    ] = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___Operation
    ]: ...
    def __init__(
        self,
        *,
        operationNames: typing___Optional[typing___Iterable[typing___Text]] = None,
        operations: typing___Optional[typing___Iterable[type___Operation]] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operationNames", b"operationNames", "operations", b"operations"
        ],
    ) -> None: ...

type___GetOperationsResponse = GetOperationsResponse

class TraceQueryParameters(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TagsEntry(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        key: typing___Text = ...
        value: typing___Text = ...
        def __init__(
            self,
            *,
            key: typing___Optional[typing___Text] = None,
            value: typing___Optional[typing___Text] = None,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions___Literal["key", b"key", "value", b"value"]
        ) -> None: ...
    type___TagsEntry = TagsEntry

    service_name: typing___Text = ...
    operation_name: typing___Text = ...
    num_traces: builtin___int = ...
    @property
    def tags(self) -> typing___MutableMapping[typing___Text, typing___Text]: ...
    @property
    def start_time_min(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    @property
    def start_time_max(self) -> google___protobuf___timestamp_pb2___Timestamp: ...
    @property
    def duration_min(self) -> google___protobuf___duration_pb2___Duration: ...
    @property
    def duration_max(self) -> google___protobuf___duration_pb2___Duration: ...
    def __init__(
        self,
        *,
        service_name: typing___Optional[typing___Text] = None,
        operation_name: typing___Optional[typing___Text] = None,
        tags: typing___Optional[typing___Mapping[typing___Text, typing___Text]] = None,
        start_time_min: typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        start_time_max: typing___Optional[google___protobuf___timestamp_pb2___Timestamp] = None,
        duration_min: typing___Optional[google___protobuf___duration_pb2___Duration] = None,
        duration_max: typing___Optional[google___protobuf___duration_pb2___Duration] = None,
        num_traces: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "duration_max",
            b"duration_max",
            "duration_min",
            b"duration_min",
            "start_time_max",
            b"start_time_max",
            "start_time_min",
            b"start_time_min",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "duration_max",
            b"duration_max",
            "duration_min",
            b"duration_min",
            "num_traces",
            b"num_traces",
            "operation_name",
            b"operation_name",
            "service_name",
            b"service_name",
            "start_time_max",
            b"start_time_max",
            "start_time_min",
            b"start_time_min",
            "tags",
            b"tags",
        ],
    ) -> None: ...

type___TraceQueryParameters = TraceQueryParameters

class FindTracesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def query(self) -> type___TraceQueryParameters: ...
    def __init__(
        self,
        *,
        query: typing___Optional[type___TraceQueryParameters] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["query", b"query"]
    ) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal["query", b"query"]) -> None: ...

type___FindTracesRequest = FindTracesRequest

class SpansResponseChunk(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def spans(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        model_pb2___Span
    ]: ...
    def __init__(
        self,
        *,
        spans: typing___Optional[typing___Iterable[model_pb2___Span]] = None,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions___Literal["spans", b"spans"]) -> None: ...

type___SpansResponseChunk = SpansResponseChunk

class FindTraceIDsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def query(self) -> type___TraceQueryParameters: ...
    def __init__(
        self,
        *,
        query: typing___Optional[type___TraceQueryParameters] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["query", b"query"]
    ) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal["query", b"query"]) -> None: ...

type___FindTraceIDsRequest = FindTraceIDsRequest

class FindTraceIDsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    trace_ids: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
        builtin___bytes
    ] = ...
    def __init__(
        self,
        *,
        trace_ids: typing___Optional[typing___Iterable[builtin___bytes]] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["trace_ids", b"trace_ids"]
    ) -> None: ...

type___FindTraceIDsResponse = FindTraceIDsResponse

class CapabilitiesRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    def __init__(
        self,
    ) -> None: ...

type___CapabilitiesRequest = CapabilitiesRequest

class CapabilitiesResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    archiveSpanReader: builtin___bool = ...
    archiveSpanWriter: builtin___bool = ...
    def __init__(
        self,
        *,
        archiveSpanReader: typing___Optional[builtin___bool] = None,
        archiveSpanWriter: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "archiveSpanReader", b"archiveSpanReader", "archiveSpanWriter", b"archiveSpanWriter"
        ],
    ) -> None: ...

type___CapabilitiesResponse = CapabilitiesResponse
