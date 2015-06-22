# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: perf_db.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import qpstest_pb2 as qpstest__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='perf_db.proto',
  package='grpc.testing',
  syntax='proto3',
  serialized_pb=_b('\n\rperf_db.proto\x12\x0cgrpc.testing\x1a\rqpstest.proto\"\x89\x02\n\x07Metrics\x12\x0b\n\x03qps\x18\x01 \x01(\x01\x12\x14\n\x0cqps_per_core\x18\x02 \x01(\x01\x12\x13\n\x0bperc_lat_50\x18\x03 \x01(\x01\x12\x13\n\x0bperc_lat_90\x18\x04 \x01(\x01\x12\x13\n\x0bperc_lat_95\x18\x05 \x01(\x01\x12\x13\n\x0bperc_lat_99\x18\x06 \x01(\x01\x12\x1b\n\x13perc_lat_99_point_9\x18\x07 \x01(\x01\x12\x1a\n\x12server_system_time\x18\x08 \x01(\x01\x12\x18\n\x10server_user_time\x18\t \x01(\x01\x12\x1a\n\x12\x63lient_system_time\x18\n \x01(\x01\x12\x18\n\x10\x63lient_user_time\x18\x0b \x01(\x01\"\xd3\x01\n\x0b\x44\x61taDetails\x12\x11\n\ttimestamp\x18\x01 \x01(\t\x12\x11\n\ttest_name\x18\x02 \x01(\t\x12\x10\n\x08sys_info\x18\x03 \x01(\t\x12&\n\x07metrics\x18\x04 \x01(\x0b\x32\x15.grpc.testing.Metrics\x12\x31\n\rclient_config\x18\x05 \x01(\x0b\x32\x1a.grpc.testing.ClientConfig\x12\x31\n\rserver_config\x18\x06 \x01(\x0b\x32\x1a.grpc.testing.ServerConfig\"\xc2\x01\n\x0bUserDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x16\n\x0everified_email\x18\x03 \x01(\x08\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x12\n\ngiven_name\x18\x05 \x01(\t\x12\x13\n\x0b\x66\x61mily_name\x18\x06 \x01(\t\x12\x0c\n\x04link\x18\x07 \x01(\t\x12\x0f\n\x07picture\x18\x08 \x01(\t\x12\x0e\n\x06gender\x18\t \x01(\t\x12\x0e\n\x06locale\x18\n \x01(\t\x12\n\n\x02hd\x18\x0b \x01(\t\"u\n\x11SingleUserDetails\x12/\n\x0c\x64\x61ta_details\x18\x01 \x03(\x0b\x32\x19.grpc.testing.DataDetails\x12/\n\x0cuser_details\x18\x02 \x01(\x0b\x32\x19.grpc.testing.UserDetails\"\xe2\x01\n\x17SingleUserRecordRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x11\n\ttest_name\x18\x02 \x01(\t\x12\x10\n\x08sys_info\x18\x03 \x01(\t\x12&\n\x07metrics\x18\x04 \x01(\x0b\x32\x15.grpc.testing.Metrics\x12\x31\n\rclient_config\x18\x05 \x01(\x0b\x32\x1a.grpc.testing.ClientConfig\x12\x31\n\rserver_config\x18\x06 \x01(\x0b\x32\x1a.grpc.testing.ServerConfig\"\x17\n\x15SingleUserRecordReply\",\n\x19SingleUserRetrieveRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"K\n\x17SingleUserRetrieveReply\x12\x30\n\x07\x64\x65tails\x18\x01 \x01(\x0b\x32\x1f.grpc.testing.SingleUserDetails\"K\n\x15\x41llUsersRetrieveReply\x12\x32\n\tuser_data\x18\x01 \x03(\x0b\x32\x1f.grpc.testing.SingleUserDetails\"\x19\n\x17\x41llUsersRetrieveRequest2\xca\x02\n\x0ePerfDbTransfer\x12\x66\n\x16RecordSingleClientData\x12%.grpc.testing.SingleUserRecordRequest\x1a#.grpc.testing.SingleUserRecordReply\"\x00\x12j\n\x16RetrieveSingleUserData\x12\'.grpc.testing.SingleUserRetrieveRequest\x1a%.grpc.testing.SingleUserRetrieveReply\"\x00\x12\x64\n\x14RetrieveAllUsersData\x12%.grpc.testing.AllUsersRetrieveRequest\x1a#.grpc.testing.AllUsersRetrieveReply\"\x00\x62\x06proto3')
  ,
  dependencies=[qpstest__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_METRICS = _descriptor.Descriptor(
  name='Metrics',
  full_name='grpc.testing.Metrics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='qps', full_name='grpc.testing.Metrics.qps', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qps_per_core', full_name='grpc.testing.Metrics.qps_per_core', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perc_lat_50', full_name='grpc.testing.Metrics.perc_lat_50', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perc_lat_90', full_name='grpc.testing.Metrics.perc_lat_90', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perc_lat_95', full_name='grpc.testing.Metrics.perc_lat_95', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perc_lat_99', full_name='grpc.testing.Metrics.perc_lat_99', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='perc_lat_99_point_9', full_name='grpc.testing.Metrics.perc_lat_99_point_9', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_system_time', full_name='grpc.testing.Metrics.server_system_time', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_user_time', full_name='grpc.testing.Metrics.server_user_time', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_system_time', full_name='grpc.testing.Metrics.client_system_time', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_user_time', full_name='grpc.testing.Metrics.client_user_time', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=312,
)


_DATADETAILS = _descriptor.Descriptor(
  name='DataDetails',
  full_name='grpc.testing.DataDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='grpc.testing.DataDetails.timestamp', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_name', full_name='grpc.testing.DataDetails.test_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sys_info', full_name='grpc.testing.DataDetails.sys_info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='grpc.testing.DataDetails.metrics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_config', full_name='grpc.testing.DataDetails.client_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_config', full_name='grpc.testing.DataDetails.server_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=315,
  serialized_end=526,
)


_USERDETAILS = _descriptor.Descriptor(
  name='UserDetails',
  full_name='grpc.testing.UserDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='grpc.testing.UserDetails.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='email', full_name='grpc.testing.UserDetails.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='verified_email', full_name='grpc.testing.UserDetails.verified_email', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc.testing.UserDetails.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='given_name', full_name='grpc.testing.UserDetails.given_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='family_name', full_name='grpc.testing.UserDetails.family_name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='link', full_name='grpc.testing.UserDetails.link', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='picture', full_name='grpc.testing.UserDetails.picture', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gender', full_name='grpc.testing.UserDetails.gender', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locale', full_name='grpc.testing.UserDetails.locale', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hd', full_name='grpc.testing.UserDetails.hd', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=723,
)


_SINGLEUSERDETAILS = _descriptor.Descriptor(
  name='SingleUserDetails',
  full_name='grpc.testing.SingleUserDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data_details', full_name='grpc.testing.SingleUserDetails.data_details', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_details', full_name='grpc.testing.SingleUserDetails.user_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=725,
  serialized_end=842,
)


_SINGLEUSERRECORDREQUEST = _descriptor.Descriptor(
  name='SingleUserRecordRequest',
  full_name='grpc.testing.SingleUserRecordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='access_token', full_name='grpc.testing.SingleUserRecordRequest.access_token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='test_name', full_name='grpc.testing.SingleUserRecordRequest.test_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sys_info', full_name='grpc.testing.SingleUserRecordRequest.sys_info', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metrics', full_name='grpc.testing.SingleUserRecordRequest.metrics', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='client_config', full_name='grpc.testing.SingleUserRecordRequest.client_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='server_config', full_name='grpc.testing.SingleUserRecordRequest.server_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=845,
  serialized_end=1071,
)


_SINGLEUSERRECORDREPLY = _descriptor.Descriptor(
  name='SingleUserRecordReply',
  full_name='grpc.testing.SingleUserRecordReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1073,
  serialized_end=1096,
)


_SINGLEUSERRETRIEVEREQUEST = _descriptor.Descriptor(
  name='SingleUserRetrieveRequest',
  full_name='grpc.testing.SingleUserRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='grpc.testing.SingleUserRetrieveRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1098,
  serialized_end=1142,
)


_SINGLEUSERRETRIEVEREPLY = _descriptor.Descriptor(
  name='SingleUserRetrieveReply',
  full_name='grpc.testing.SingleUserRetrieveReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='details', full_name='grpc.testing.SingleUserRetrieveReply.details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1219,
)


_ALLUSERSRETRIEVEREPLY = _descriptor.Descriptor(
  name='AllUsersRetrieveReply',
  full_name='grpc.testing.AllUsersRetrieveReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_data', full_name='grpc.testing.AllUsersRetrieveReply.user_data', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1221,
  serialized_end=1296,
)


_ALLUSERSRETRIEVEREQUEST = _descriptor.Descriptor(
  name='AllUsersRetrieveRequest',
  full_name='grpc.testing.AllUsersRetrieveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1298,
  serialized_end=1323,
)

_DATADETAILS.fields_by_name['metrics'].message_type = _METRICS
_DATADETAILS.fields_by_name['client_config'].message_type = qpstest__pb2._CLIENTCONFIG
_DATADETAILS.fields_by_name['server_config'].message_type = qpstest__pb2._SERVERCONFIG
_SINGLEUSERDETAILS.fields_by_name['data_details'].message_type = _DATADETAILS
_SINGLEUSERDETAILS.fields_by_name['user_details'].message_type = _USERDETAILS
_SINGLEUSERRECORDREQUEST.fields_by_name['metrics'].message_type = _METRICS
_SINGLEUSERRECORDREQUEST.fields_by_name['client_config'].message_type = qpstest__pb2._CLIENTCONFIG
_SINGLEUSERRECORDREQUEST.fields_by_name['server_config'].message_type = qpstest__pb2._SERVERCONFIG
_SINGLEUSERRETRIEVEREPLY.fields_by_name['details'].message_type = _SINGLEUSERDETAILS
_ALLUSERSRETRIEVEREPLY.fields_by_name['user_data'].message_type = _SINGLEUSERDETAILS
DESCRIPTOR.message_types_by_name['Metrics'] = _METRICS
DESCRIPTOR.message_types_by_name['DataDetails'] = _DATADETAILS
DESCRIPTOR.message_types_by_name['UserDetails'] = _USERDETAILS
DESCRIPTOR.message_types_by_name['SingleUserDetails'] = _SINGLEUSERDETAILS
DESCRIPTOR.message_types_by_name['SingleUserRecordRequest'] = _SINGLEUSERRECORDREQUEST
DESCRIPTOR.message_types_by_name['SingleUserRecordReply'] = _SINGLEUSERRECORDREPLY
DESCRIPTOR.message_types_by_name['SingleUserRetrieveRequest'] = _SINGLEUSERRETRIEVEREQUEST
DESCRIPTOR.message_types_by_name['SingleUserRetrieveReply'] = _SINGLEUSERRETRIEVEREPLY
DESCRIPTOR.message_types_by_name['AllUsersRetrieveReply'] = _ALLUSERSRETRIEVEREPLY
DESCRIPTOR.message_types_by_name['AllUsersRetrieveRequest'] = _ALLUSERSRETRIEVEREQUEST

Metrics = _reflection.GeneratedProtocolMessageType('Metrics', (_message.Message,), dict(
  DESCRIPTOR = _METRICS,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.Metrics)
  ))
_sym_db.RegisterMessage(Metrics)

DataDetails = _reflection.GeneratedProtocolMessageType('DataDetails', (_message.Message,), dict(
  DESCRIPTOR = _DATADETAILS,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.DataDetails)
  ))
_sym_db.RegisterMessage(DataDetails)

UserDetails = _reflection.GeneratedProtocolMessageType('UserDetails', (_message.Message,), dict(
  DESCRIPTOR = _USERDETAILS,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.UserDetails)
  ))
_sym_db.RegisterMessage(UserDetails)

SingleUserDetails = _reflection.GeneratedProtocolMessageType('SingleUserDetails', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEUSERDETAILS,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.SingleUserDetails)
  ))
_sym_db.RegisterMessage(SingleUserDetails)

SingleUserRecordRequest = _reflection.GeneratedProtocolMessageType('SingleUserRecordRequest', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEUSERRECORDREQUEST,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.SingleUserRecordRequest)
  ))
_sym_db.RegisterMessage(SingleUserRecordRequest)

SingleUserRecordReply = _reflection.GeneratedProtocolMessageType('SingleUserRecordReply', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEUSERRECORDREPLY,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.SingleUserRecordReply)
  ))
_sym_db.RegisterMessage(SingleUserRecordReply)

SingleUserRetrieveRequest = _reflection.GeneratedProtocolMessageType('SingleUserRetrieveRequest', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEUSERRETRIEVEREQUEST,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.SingleUserRetrieveRequest)
  ))
_sym_db.RegisterMessage(SingleUserRetrieveRequest)

SingleUserRetrieveReply = _reflection.GeneratedProtocolMessageType('SingleUserRetrieveReply', (_message.Message,), dict(
  DESCRIPTOR = _SINGLEUSERRETRIEVEREPLY,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.SingleUserRetrieveReply)
  ))
_sym_db.RegisterMessage(SingleUserRetrieveReply)

AllUsersRetrieveReply = _reflection.GeneratedProtocolMessageType('AllUsersRetrieveReply', (_message.Message,), dict(
  DESCRIPTOR = _ALLUSERSRETRIEVEREPLY,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.AllUsersRetrieveReply)
  ))
_sym_db.RegisterMessage(AllUsersRetrieveReply)

AllUsersRetrieveRequest = _reflection.GeneratedProtocolMessageType('AllUsersRetrieveRequest', (_message.Message,), dict(
  DESCRIPTOR = _ALLUSERSRETRIEVEREQUEST,
  __module__ = 'perf_db_pb2'
  # @@protoc_insertion_point(class_scope:grpc.testing.AllUsersRetrieveRequest)
  ))
_sym_db.RegisterMessage(AllUsersRetrieveRequest)


import abc
from grpc.early_adopter import implementations
from grpc.framework.alpha import utilities
class EarlyAdopterPerfDbTransferServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def RecordSingleClientData(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RetrieveSingleUserData(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def RetrieveAllUsersData(self, request, context):
    raise NotImplementedError()
class EarlyAdopterPerfDbTransferServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterPerfDbTransferStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def RecordSingleClientData(self, request):
    raise NotImplementedError()
  RecordSingleClientData.async = None
  @abc.abstractmethod
  def RetrieveSingleUserData(self, request):
    raise NotImplementedError()
  RetrieveSingleUserData.async = None
  @abc.abstractmethod
  def RetrieveAllUsersData(self, request):
    raise NotImplementedError()
  RetrieveAllUsersData.async = None
def early_adopter_create_PerfDbTransfer_server(servicer, port, private_key=None, certificate_chain=None):
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  method_service_descriptions = {
    "RecordSingleClientData": utilities.unary_unary_service_description(
      servicer.RecordSingleClientData,
      perf_db_pb2.SingleUserRecordRequest.FromString,
      perf_db_pb2.SingleUserRecordReply.SerializeToString,
    ),
    "RetrieveAllUsersData": utilities.unary_unary_service_description(
      servicer.RetrieveAllUsersData,
      perf_db_pb2.AllUsersRetrieveRequest.FromString,
      perf_db_pb2.AllUsersRetrieveReply.SerializeToString,
    ),
    "RetrieveSingleUserData": utilities.unary_unary_service_description(
      servicer.RetrieveSingleUserData,
      perf_db_pb2.SingleUserRetrieveRequest.FromString,
      perf_db_pb2.SingleUserRetrieveReply.SerializeToString,
    ),
  }
  return implementations.server("grpc.testing.PerfDbTransfer", method_service_descriptions, port, private_key=private_key, certificate_chain=certificate_chain)
def early_adopter_create_PerfDbTransfer_stub(host, port, metadata_transformer=None, secure=False, root_certificates=None, private_key=None, certificate_chain=None, server_host_override=None):
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  import perf_db_pb2
  method_invocation_descriptions = {
    "RecordSingleClientData": utilities.unary_unary_invocation_description(
      perf_db_pb2.SingleUserRecordRequest.SerializeToString,
      perf_db_pb2.SingleUserRecordReply.FromString,
    ),
    "RetrieveAllUsersData": utilities.unary_unary_invocation_description(
      perf_db_pb2.AllUsersRetrieveRequest.SerializeToString,
      perf_db_pb2.AllUsersRetrieveReply.FromString,
    ),
    "RetrieveSingleUserData": utilities.unary_unary_invocation_description(
      perf_db_pb2.SingleUserRetrieveRequest.SerializeToString,
      perf_db_pb2.SingleUserRetrieveReply.FromString,
    ),
  }
  return implementations.stub("grpc.testing.PerfDbTransfer", method_invocation_descriptions, host, port, metadata_transformer=metadata_transformer, secure=secure, root_certificates=root_certificates, private_key=private_key, certificate_chain=certificate_chain, server_host_override=server_host_override)
# @@protoc_insertion_point(module_scope)
