#
# Copyright 2015 Google Inc. All Rights Reserved.
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
"""View for the fronted."""

from django.shortcuts import render

from user_data import UserData

user_data = UserData()


def display_performance_database(request):
  """View for performance database table page."""
  data = all_users_data()
  return render(request, 'data_table.html', {'all_users_data': data})


def display_configs(request):
  """View for config page."""
  return render(request, 'configs.html', {})


def display_general_statistic(request, metric):
  """View for general statistic page."""
  return general_statistic_renderer(request, metric)


def general_statistic_renderer(request, metric):
  """General statistic page renderer."""
  data = all_users_single_metric_data(metric)
  return render(request, 'general_plots.html',
                {'metric': get_metric_full_desc(metric),
                 'all_users_data': data})


def display_user_metrics(request, client_id):
  """View for user metrics page."""
  complete_data = single_user_data(client_id)
  return render(request, 'user_plots.html',
                {'username': complete_data[0],
                 'user_data': complete_data[1]})


def get_metric_full_desc(metric):
  """Returns full metric name."""

  metric_name = {
      'qps': 'Queries Per Second',
      'qpspercore': 'QPS Per Core',
      'perc50': '50th Percentile Latency',
      'perc90': '90th Percentile Latency',
      'perc95': '95th Percentile Latency',
      'perc99': '99th Percentile Latency',
      'perc99point9': '99.9th Percentile Latency',
      'serversystime': 'Server System Time',
      'serverusertime': 'Server User Time',
      'clientsystime': 'Client System Time',
      'clientusertime': 'Client User Time'
  }.get(metric, 'error')

  if metric_name == 'error':
    raise Exception

  return metric_name


def single_user_data(client_id):
  """Returns single user data."""
  return user_data.get_single_user_data(client_id)


def all_users_data():
  """Returns all users' data."""
  return user_data.get_all_users_data()


def all_users_single_metric_data(metric):
  """Return all users' single metric data."""
  return user_data.get_all_users_single_metric_data(metric)
