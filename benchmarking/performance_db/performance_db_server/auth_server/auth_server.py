#!/usr/bin/python
#
# Copyright 2015, Google Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of Google Inc. nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import auth_user_pb2
import argparse
import sys
import time
from oauth2client import tools
from oauth2client import client
from oauth2client.file import Storage
from apiclient.discovery import build
import httplib2
import leveldb
import os
import hashlib
import uuid

parser = argparse.ArgumentParser(description='Report metrics to performance database')
parser.add_argument('--port', type=int, default='2817', help='Port of authentication server')
parser.add_argument('--id_name_database', type=str, default=os.path.expanduser('~')+'/.grpc/id_name', help='Location of id to username database')
parser.add_argument('--name_id_database', type=str, default=os.path.expanduser('~')+'/.grpc/name_id', help='Location of username to id database')

args = parser.parse_args()

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class AuthenticationServicer(auth_user_pb2.EarlyAdopterAuthenticationServicer):
  def __init__(self):
    # Setting hashed id to username database
    if not os.path.exists(args.id_name_database):
      os.makedirs(args.id_name_database)
    self.id_name_db = leveldb.LevelDB(args.id_name_database)
    
    # Setting username to hashed id database
    if not os.path.exists(args.name_id_database):
      os.makedirs(args.name_id_database)
    self.name_id_db = leveldb.LevelDB(args.name_id_database)

  # Authenticate the user, creating entries in database as required
  def AuthenticateUser(self, request, context):
    file_name = str(uuid.uuid4()) # generate random temporary file name to store credentials

    # Write credentials to file
    with open(file_name, 'wb') as output:
      output.write(request.credentials)

    # Extract credentials from file
    storage = Storage(file_name)
    credentials = storage.get()

    os.remove(file_name) # Remove temporary file

    # Get hashed id from credentials
    http_auth = credentials.authorize(httplib2.Http())
    auth_service = build('oauth2', 'v2', http=http_auth)

    user_info = auth_service.userinfo().get().execute()
    hash_object = hashlib.md5(user_info.get('id'))
    hashed_id = hash_object.hexdigest()

    reply = auth_user_pb2.AuthenticateUserReply()

    # Store username against user id, if username is unique
    try:
      stored_id = self.name_id_db.Get(request.username)
      if stored_id != hashed_id:
        reply.is_unique_username = False
      else:
        reply.is_unique_username = True
    # If username is unique
    except KeyError, e:
      # Free the previous username assigned to this user, if applicable
      try:
        existing_username = self.id_name_db.Get(hashed_id)
        self.name_id_db.Delete(existing_username)
      except KeyError, e:
        pass

      # create required entries in both databases
      self.id_name_db.Put(hashed_id, request.username)
      self.name_id_db.Put(request.username, hashed_id)

      reply.is_unique_username = True

    return reply

  # Return username based on hashed user id
  def ConfirmUser(self, request, context):
    reply = auth_user_pb2.ConfirmUserReply()

    # Get username for given hashed id
    try:
      username = self.id_name_db.Get(request.hashed_id)

      reply.is_authenticated = True
      reply.username = username
    # If hashed is not present in database
    except KeyError, e:
      reply.is_authenticated = False

    return reply

def serve(argv):
  # Create and start server
  server = auth_user_pb2.early_adopter_create_Authentication_server(AuthenticationServicer(), args.port, None, None)
  server.start()

  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop()

if __name__ == '__main__':
  serve(sys.argv)