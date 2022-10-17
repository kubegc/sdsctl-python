# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import cmdcall_pb2 as cmdcall__pb2


class CmdCallStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Call = channel.unary_unary(
                '/cmdcall.CmdCall/Call',
                request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
                response_deserializer=cmdcall__pb2.CallResponse.FromString,
                )
        self.CallWithResult = channel.unary_unary(
                '/cmdcall.CmdCall/CallWithResult',
                request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
                response_deserializer=cmdcall__pb2.CallResponse.FromString,
                )
        self.CallAndTransferXmlToJson = channel.unary_unary(
                '/cmdcall.CmdCall/CallAndTransferXmlToJson',
                request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
                response_deserializer=cmdcall__pb2.CallResponse.FromString,
                )
        self.CallAndSplitKVToJson = channel.unary_unary(
                '/cmdcall.CmdCall/CallAndSplitKVToJson',
                request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
                response_deserializer=cmdcall__pb2.CallResponse.FromString,
                )
        self.CallAndGetOutput = channel.unary_unary(
                '/cmdcall.CmdCall/CallAndGetOutput',
                request_serializer=cmdcall__pb2.CallRequest.SerializeToString,
                response_deserializer=cmdcall__pb2.CallResponse.FromString,
                )


class CmdCallServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Call(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallWithResult(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallAndTransferXmlToJson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallAndSplitKVToJson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CallAndGetOutput(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CmdCallServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Call': grpc.unary_unary_rpc_method_handler(
                    servicer.Call,
                    request_deserializer=cmdcall__pb2.CallRequest.FromString,
                    response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
            ),
            'CallWithResult': grpc.unary_unary_rpc_method_handler(
                    servicer.CallWithResult,
                    request_deserializer=cmdcall__pb2.CallRequest.FromString,
                    response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
            ),
            'CallAndTransferXmlToJson': grpc.unary_unary_rpc_method_handler(
                    servicer.CallAndTransferXmlToJson,
                    request_deserializer=cmdcall__pb2.CallRequest.FromString,
                    response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
            ),
            'CallAndSplitKVToJson': grpc.unary_unary_rpc_method_handler(
                    servicer.CallAndSplitKVToJson,
                    request_deserializer=cmdcall__pb2.CallRequest.FromString,
                    response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
            ),
            'CallAndGetOutput': grpc.unary_unary_rpc_method_handler(
                    servicer.CallAndGetOutput,
                    request_deserializer=cmdcall__pb2.CallRequest.FromString,
                    response_serializer=cmdcall__pb2.CallResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cmdcall.CmdCall', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class CmdCall(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Call(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cmdcall.CmdCall/Call',
            cmdcall__pb2.CallRequest.SerializeToString,
            cmdcall__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CallWithResult(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cmdcall.CmdCall/CallWithResult',
            cmdcall__pb2.CallRequest.SerializeToString,
            cmdcall__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CallAndTransferXmlToJson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cmdcall.CmdCall/CallAndTransferXmlToJson',
            cmdcall__pb2.CallRequest.SerializeToString,
            cmdcall__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CallAndSplitKVToJson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cmdcall.CmdCall/CallAndSplitKVToJson',
            cmdcall__pb2.CallRequest.SerializeToString,
            cmdcall__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CallAndGetOutput(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cmdcall.CmdCall/CallAndGetOutput',
            cmdcall__pb2.CallRequest.SerializeToString,
            cmdcall__pb2.CallResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
