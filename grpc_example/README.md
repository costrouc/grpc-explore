# Development

Create the python definitions for client/server

```shell
python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_pthon_out=. todo.proto
```

Python server `todo_server.py` used for serving 

```shell
python -m grpc_example.todo_server
```

In a separate terminal run

```shell
python -m grpc_example.todo_client
```