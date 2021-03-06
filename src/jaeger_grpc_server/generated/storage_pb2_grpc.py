# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
# flake8: noqa
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import jaeger_grpc_server.generated.storage_pb2 as storage__pb2


class SpanWriterPluginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WriteSpan = channel.unary_unary(
            "/jaeger.storage.v1.SpanWriterPlugin/WriteSpan",
            request_serializer=storage__pb2.WriteSpanRequest.SerializeToString,
            response_deserializer=storage__pb2.WriteSpanResponse.FromString,
        )


class SpanWriterPluginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WriteSpan(self, request, context):
        """spanstore/Writer"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SpanWriterPluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "WriteSpan": grpc.unary_unary_rpc_method_handler(
            servicer.WriteSpan,
            request_deserializer=storage__pb2.WriteSpanRequest.FromString,
            response_serializer=storage__pb2.WriteSpanResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "jaeger.storage.v1.SpanWriterPlugin", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SpanWriterPlugin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WriteSpan(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/jaeger.storage.v1.SpanWriterPlugin/WriteSpan",
            storage__pb2.WriteSpanRequest.SerializeToString,
            storage__pb2.WriteSpanResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class SpanReaderPluginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTrace = channel.unary_stream(
            "/jaeger.storage.v1.SpanReaderPlugin/GetTrace",
            request_serializer=storage__pb2.GetTraceRequest.SerializeToString,
            response_deserializer=storage__pb2.SpansResponseChunk.FromString,
        )
        self.GetServices = channel.unary_unary(
            "/jaeger.storage.v1.SpanReaderPlugin/GetServices",
            request_serializer=storage__pb2.GetServicesRequest.SerializeToString,
            response_deserializer=storage__pb2.GetServicesResponse.FromString,
        )
        self.GetOperations = channel.unary_unary(
            "/jaeger.storage.v1.SpanReaderPlugin/GetOperations",
            request_serializer=storage__pb2.GetOperationsRequest.SerializeToString,
            response_deserializer=storage__pb2.GetOperationsResponse.FromString,
        )
        self.FindTraces = channel.unary_stream(
            "/jaeger.storage.v1.SpanReaderPlugin/FindTraces",
            request_serializer=storage__pb2.FindTracesRequest.SerializeToString,
            response_deserializer=storage__pb2.SpansResponseChunk.FromString,
        )
        self.FindTraceIDs = channel.unary_unary(
            "/jaeger.storage.v1.SpanReaderPlugin/FindTraceIDs",
            request_serializer=storage__pb2.FindTraceIDsRequest.SerializeToString,
            response_deserializer=storage__pb2.FindTraceIDsResponse.FromString,
        )


class SpanReaderPluginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTrace(self, request, context):
        """spanstore/Reader"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetServices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetOperations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FindTraces(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def FindTraceIDs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_SpanReaderPluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetTrace": grpc.unary_stream_rpc_method_handler(
            servicer.GetTrace,
            request_deserializer=storage__pb2.GetTraceRequest.FromString,
            response_serializer=storage__pb2.SpansResponseChunk.SerializeToString,
        ),
        "GetServices": grpc.unary_unary_rpc_method_handler(
            servicer.GetServices,
            request_deserializer=storage__pb2.GetServicesRequest.FromString,
            response_serializer=storage__pb2.GetServicesResponse.SerializeToString,
        ),
        "GetOperations": grpc.unary_unary_rpc_method_handler(
            servicer.GetOperations,
            request_deserializer=storage__pb2.GetOperationsRequest.FromString,
            response_serializer=storage__pb2.GetOperationsResponse.SerializeToString,
        ),
        "FindTraces": grpc.unary_stream_rpc_method_handler(
            servicer.FindTraces,
            request_deserializer=storage__pb2.FindTracesRequest.FromString,
            response_serializer=storage__pb2.SpansResponseChunk.SerializeToString,
        ),
        "FindTraceIDs": grpc.unary_unary_rpc_method_handler(
            servicer.FindTraceIDs,
            request_deserializer=storage__pb2.FindTraceIDsRequest.FromString,
            response_serializer=storage__pb2.FindTraceIDsResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "jaeger.storage.v1.SpanReaderPlugin", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class SpanReaderPlugin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTrace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/jaeger.storage.v1.SpanReaderPlugin/GetTrace",
            storage__pb2.GetTraceRequest.SerializeToString,
            storage__pb2.SpansResponseChunk.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetServices(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/jaeger.storage.v1.SpanReaderPlugin/GetServices",
            storage__pb2.GetServicesRequest.SerializeToString,
            storage__pb2.GetServicesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetOperations(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/jaeger.storage.v1.SpanReaderPlugin/GetOperations",
            storage__pb2.GetOperationsRequest.SerializeToString,
            storage__pb2.GetOperationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def FindTraces(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/jaeger.storage.v1.SpanReaderPlugin/FindTraces",
            storage__pb2.FindTracesRequest.SerializeToString,
            storage__pb2.SpansResponseChunk.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def FindTraceIDs(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/jaeger.storage.v1.SpanReaderPlugin/FindTraceIDs",
            storage__pb2.FindTraceIDsRequest.SerializeToString,
            storage__pb2.FindTraceIDsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class ArchiveSpanWriterPluginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WriteArchiveSpan = channel.unary_unary(
            "/jaeger.storage.v1.ArchiveSpanWriterPlugin/WriteArchiveSpan",
            request_serializer=storage__pb2.WriteSpanRequest.SerializeToString,
            response_deserializer=storage__pb2.WriteSpanResponse.FromString,
        )


class ArchiveSpanWriterPluginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WriteArchiveSpan(self, request, context):
        """spanstore/Writer"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ArchiveSpanWriterPluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "WriteArchiveSpan": grpc.unary_unary_rpc_method_handler(
            servicer.WriteArchiveSpan,
            request_deserializer=storage__pb2.WriteSpanRequest.FromString,
            response_serializer=storage__pb2.WriteSpanResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "jaeger.storage.v1.ArchiveSpanWriterPlugin", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ArchiveSpanWriterPlugin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WriteArchiveSpan(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/jaeger.storage.v1.ArchiveSpanWriterPlugin/WriteArchiveSpan",
            storage__pb2.WriteSpanRequest.SerializeToString,
            storage__pb2.WriteSpanResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class ArchiveSpanReaderPluginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetArchiveTrace = channel.unary_stream(
            "/jaeger.storage.v1.ArchiveSpanReaderPlugin/GetArchiveTrace",
            request_serializer=storage__pb2.GetTraceRequest.SerializeToString,
            response_deserializer=storage__pb2.SpansResponseChunk.FromString,
        )


class ArchiveSpanReaderPluginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetArchiveTrace(self, request, context):
        """spanstore/Reader"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_ArchiveSpanReaderPluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetArchiveTrace": grpc.unary_stream_rpc_method_handler(
            servicer.GetArchiveTrace,
            request_deserializer=storage__pb2.GetTraceRequest.FromString,
            response_serializer=storage__pb2.SpansResponseChunk.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "jaeger.storage.v1.ArchiveSpanReaderPlugin", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ArchiveSpanReaderPlugin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetArchiveTrace(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/jaeger.storage.v1.ArchiveSpanReaderPlugin/GetArchiveTrace",
            storage__pb2.GetTraceRequest.SerializeToString,
            storage__pb2.SpansResponseChunk.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class DependenciesReaderPluginStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetDependencies = channel.unary_unary(
            "/jaeger.storage.v1.DependenciesReaderPlugin/GetDependencies",
            request_serializer=storage__pb2.GetDependenciesRequest.SerializeToString,
            response_deserializer=storage__pb2.GetDependenciesResponse.FromString,
        )


class DependenciesReaderPluginServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetDependencies(self, request, context):
        """dependencystore/Reader"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_DependenciesReaderPluginServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "GetDependencies": grpc.unary_unary_rpc_method_handler(
            servicer.GetDependencies,
            request_deserializer=storage__pb2.GetDependenciesRequest.FromString,
            response_serializer=storage__pb2.GetDependenciesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "jaeger.storage.v1.DependenciesReaderPlugin", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DependenciesReaderPlugin(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetDependencies(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/jaeger.storage.v1.DependenciesReaderPlugin/GetDependencies",
            storage__pb2.GetDependenciesRequest.SerializeToString,
            storage__pb2.GetDependenciesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )


class PluginCapabilitiesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Capabilities = channel.unary_unary(
            "/jaeger.storage.v1.PluginCapabilities/Capabilities",
            request_serializer=storage__pb2.CapabilitiesRequest.SerializeToString,
            response_deserializer=storage__pb2.CapabilitiesResponse.FromString,
        )


class PluginCapabilitiesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Capabilities(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PluginCapabilitiesServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Capabilities": grpc.unary_unary_rpc_method_handler(
            servicer.Capabilities,
            request_deserializer=storage__pb2.CapabilitiesRequest.FromString,
            response_serializer=storage__pb2.CapabilitiesResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "jaeger.storage.v1.PluginCapabilities", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PluginCapabilities(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Capabilities(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/jaeger.storage.v1.PluginCapabilities/Capabilities",
            storage__pb2.CapabilitiesRequest.SerializeToString,
            storage__pb2.CapabilitiesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
