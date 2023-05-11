# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import sending_pb2 as sending__pb2


class SenderCSVStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendFile = channel.unary_unary(
                '/SenderCSV/SendFile',
                request_serializer=sending__pb2.SendRequest.SerializeToString,
                response_deserializer=sending__pb2.SendResponse.FromString,
                )


class SenderCSVServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendFile(self, request, context):
        """recieves token, team name, timestamp
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SenderCSVServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendFile': grpc.unary_unary_rpc_method_handler(
                    servicer.SendFile,
                    request_deserializer=sending__pb2.SendRequest.FromString,
                    response_serializer=sending__pb2.SendResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SenderCSV', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SenderCSV(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/SenderCSV/SendFile',
            sending__pb2.SendRequest.SerializeToString,
            sending__pb2.SendResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)