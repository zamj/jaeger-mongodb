"""The span writer grpc service implementation."""
from __future__ import annotations

from grpc import ServicerContext

from jaeger_grpc_server.db.mongo_client import MongoWrapper
from jaeger_grpc_server.generated.storage_pb2 import WriteSpanRequest, WriteSpanResponse
from jaeger_grpc_server.generated.storage_pb2_grpc import SpanWriterPluginServicer


class SpanWriterService(SpanWriterPluginServicer):
    """The SpanWriter grpc service implementation."""

    def __init__(self, db: MongoWrapper):
        """
        Create an instance of the SpanWriterService.

        :param db: A MongoWrapper instance.
        """
        self.db = db

    def WriteSpan(self, request: WriteSpanRequest, context: ServicerContext) -> WriteSpanResponse:
        """
        Write the given span to the database.

        :param request: The request containing the Span to store.
        :param context: The grpc context of the request.
        :return: A WriteSpanResponse. Contains nothing inside of it.
        """
        self.db.span_collection.add_span(request.span)
        return WriteSpanResponse()
