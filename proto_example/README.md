# Development

To genereate the python protobuf file

```shell
protoc -I . --python_out=. --pyi_out=. employees.proto
```

This will create a `employees_pb2.py` file. See the example for how to interact with the library. See [comparison of protobuf vs. json](https://nilsmagnus.github.io/post/proto-json-sizes/) for size comparisons.
