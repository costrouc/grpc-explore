# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntodo.proto\x12\x0btodoPackage\"\x07\n\x05\x45mpty\"$\n\x08TodoItem\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\"1\n\tTodoItems\x12$\n\x05items\x18\x01 \x03(\x0b\x32\x15.todoPackage.TodoItem2\xbb\x01\n\x04Todo\x12:\n\ncreateTodo\x12\x15.todoPackage.TodoItem\x1a\x15.todoPackage.TodoItem\x12\x37\n\treadTodos\x12\x12.todoPackage.Empty\x1a\x16.todoPackage.TodoItems\x12>\n\x0freadTodosStream\x12\x12.todoPackage.Empty\x1a\x15.todoPackage.TodoItem0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'todo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPTY']._serialized_start=27
  _globals['_EMPTY']._serialized_end=34
  _globals['_TODOITEM']._serialized_start=36
  _globals['_TODOITEM']._serialized_end=72
  _globals['_TODOITEMS']._serialized_start=74
  _globals['_TODOITEMS']._serialized_end=123
  _globals['_TODO']._serialized_start=126
  _globals['_TODO']._serialized_end=313
# @@protoc_insertion_point(module_scope)
