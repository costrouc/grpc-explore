import grpc

from grpc_example import todo_pb2_grpc

def serve():
    server= grpc.server()
    todo_pb2_grpc.add_TodoServicer_to_Server(todo_pb2_grpc.TodoServicer(), server)
