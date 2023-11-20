import json

import employees_pb2

employees = [
    {
        "name": "Chris",
        "salary": 1000,
        "id": 101
    },
    {
        "name": "Foo",
        "salary": 1001,
        "id": 102
    },
    {
        "name": "Biz",
        "salary": 1002,
        "id": 103
    }
]

data = json.dumps(employees)
print(f"json data {len(data)} bytes")

employees = employees_pb2.Employees(
    employees=[
        employees_pb2.Employee(
            name="Chris",
            salary=1000,
            id=101,
        ),
        employees_pb2.Employee(
            name="Foo",
            salary=1001,
            id=102,
        ),
        employees_pb2.Employee(
            name="Biz",
            salary=1002,
            id=103,
        ),
    ],
)

data = employees.SerializeToString()
print("protobuf data", len(data), 'bytes')

new_employees = employees_pb2.Employees()
new_employees.ParseFromString(data)



