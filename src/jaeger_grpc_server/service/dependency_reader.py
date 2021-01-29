"""The dependency reader grpc service implementation."""
from __future__ import annotations

from grpc import ServicerContext

from jaeger_grpc_server.db.mongo_client import MongoWrapper
from jaeger_grpc_server.generated.storage_pb2 import GetDependenciesRequest, GetDependenciesResponse
from jaeger_grpc_server.generated.storage_pb2_grpc import DependenciesReaderPluginServicer


class DependencyReaderService(DependenciesReaderPluginServicer):
    """The DependencyReaderService grpc service implementation."""

    def __init__(self, db: MongoWrapper):
        """
        Create an instance of the DependencyReaderService.

        :param db: A MongoWrapper instance.
        """
        self.db = db

    def GetDependencies(
        self, request: GetDependenciesRequest, context: ServicerContext
    ) -> GetDependenciesResponse:
        """
        Get the dependencies between the services found in the stored spans.

        :param request: A request containing a start_time and an end_time.
        :param context: The grpc context of the request.
        :return: A GetDependenciesResponse containing a list of all the found dependencies.
        """
        links = self.db.span_collection.find_dependencies(
            start_time=request.start_time, end_time=request.end_time
        )
        return GetDependenciesResponse(dependencies=links)
