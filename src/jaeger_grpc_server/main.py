#!/usr/bin/env python
"""Entry point for the grpc server."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from sys import stdout

import grpc
from grpc_health.v1 import health_pb2, health_pb2_grpc
from grpc_health.v1.health import HealthServicer

from jaeger_grpc_server.config.config import Config
from jaeger_grpc_server.db.mongo_client import MongoWrapper
from jaeger_grpc_server.generated.storage_pb2_grpc import (
    add_DependenciesReaderPluginServicer_to_server,
    add_SpanReaderPluginServicer_to_server,
    add_SpanWriterPluginServicer_to_server,
)
from jaeger_grpc_server.service.dependency_reader import DependencyReaderService
from jaeger_grpc_server.service.span_reader import SpanReaderService
from jaeger_grpc_server.service.span_writer import SpanWriterService


def serve() -> None:
    """Set up the grpc server and start serving."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, nargs="?", help="Location of config file")

    args = parser.parse_args()
    config = None
    if args.config and args.config != "":
        config = Config.from_yaml_file(args.config)
    else:
        config = Config()
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    server.add_insecure_port(f"127.0.0.1:{config.grpc_port}")

    mongo = MongoWrapper.from_uri(config.mongo_url)
    mongo.initialize_db()

    # Add all the grpc services to the server.
    span_writer = SpanWriterService(mongo)
    add_SpanWriterPluginServicer_to_server(span_writer, server)
    span_reader = SpanReaderService(mongo)
    add_SpanReaderPluginServicer_to_server(span_reader, server)
    dependency_reader = DependencyReaderService(mongo)
    add_DependenciesReaderPluginServicer_to_server(dependency_reader, server)

    # We need to add a health service to work with the go-plugin.
    # https://github.com/hashicorp/go-plugin/blob/master/docs/guide-plugin-write-non-go.md#3-add-the-grpc-health-checking-service
    health = HealthServicer()
    health.set("plugin", health_pb2.HealthCheckResponse.ServingStatus.Value("SERVING"))
    health_pb2_grpc.add_HealthServicer_to_server(health, server)

    server.start()

    # # We need to output the handshake information so that the go plugin knows where to find us.
    # # https://github.com/hashicorp/go-plugin/blob/master/docs/guide-plugin-write-non-go.md#4-output-handshake-information
    print(f"1|1|tcp|127.0.0.1:{config.grpc_port}|grpc")

    stdout.flush()

    server.wait_for_termination()


if __name__ == "__main__":
    serve()
