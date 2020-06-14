# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging
import uuid

import grpc

import helloworld_pb2
import helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def __init__(self, server_uuid):
        self.guid = server_uuid
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, {}. Server: {}!'.format(request.name, str(self.guid)))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    server_guid = uuid.uuid4()
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(server_guid), server)
    port = 50051
    server.add_insecure_port('[::]:' + str(port))
    logging.info("Server {} starting on port {}...".format(str(server_guid), str(port)))
    server.start()
    server.wait_for_termination()
    logging.info("Server stoped.")


if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    serve()
