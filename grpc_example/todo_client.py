import grpc

from grpc_example import todo_pb2_grpc, todo_pb2


class TodoClient:
    def __init__(self):
        self.host = "localhost"
        self.port = 50051

        # instantiate a channel        
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')

        # bind the client and the server
        self.stub = todo_pb2_grpc.TodoStub(self.channel)

    def createTodo(self, id: int, text: str) -> todo_pb2.TodoItem:
        response: todo_pb2.TodoItem = self.stub.createTodo(todo_pb2.TodoItem(id=id, text=text))
        print(response)
        return response

    def readTodos(self) -> todo_pb2.TodoItems:
        response: todo_pb2.TodoItems = self.stub.readTodos(todo_pb2.Empty())
        return response

    def readTodosStream(self) -> todo_pb2.TodoItems:
        todos = []
        response = self.stub.readTodosStream(todo_pb2.Empty())
        breakpoint()
        for todo in response:
            todos.append(todo)
        return todos



t = TodoClient()
t.createTodo(id=101, text="A todo item")
print(t.readTodos())
print(t.readTodosStream())