import time
import concurrent.futures

import grpc


from grpc_example import todo_pb2_grpc, todo_pb2

TODOS = []


class TodoService(todo_pb2_grpc.TodoServicer):
    def __init__(self, *args, **kwargs):
        pass

    # request / response (think HTTP GET)
    def createTodo(self, request: todo_pb2.TodoItem, context) -> todo_pb2.TodoItem:
        print("createTodo")
        TODOS.append(request)
        return request

    # request / response (think HTTP GET)
    def readTodos(self, request: todo_pb2.Empty, context) -> todo_pb2.TodoItems:
        print("readTodos")
        return todo_pb2.TodoItems(items=TODOS)
    
    # request / multiple response (think HTTP SSE)
    def readTodosStream(self, request: todo_pb2.Empty, context):
        print("readTodosStream")
        for todo in TODOS:
            yield todo


def serve_todo():
    server= grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve_todo()