# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: image_generator.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'image_generator.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15image_generator.proto\x12\x0eimagegenerator\"\x1e\n\x0cImageRequest\x12\x0e\n\x06prompt\x18\x01 \x01(\t\"\x1e\n\rImageResponse\x12\r\n\x05image\x18\x01 \x01(\x0c\x32^\n\x0eImageGenerator\x12L\n\rGenerateImage\x12\x1c.imagegenerator.ImageRequest\x1a\x1d.imagegenerator.ImageResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'image_generator_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IMAGEREQUEST']._serialized_start=41
  _globals['_IMAGEREQUEST']._serialized_end=71
  _globals['_IMAGERESPONSE']._serialized_start=73
  _globals['_IMAGERESPONSE']._serialized_end=103
  _globals['_IMAGEGENERATOR']._serialized_start=105
  _globals['_IMAGEGENERATOR']._serialized_end=199
# @@protoc_insertion_point(module_scope)
