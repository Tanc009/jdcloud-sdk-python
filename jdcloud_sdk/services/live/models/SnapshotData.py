# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.


class SnapshotData(object):

    def __init__(self, publishDomain=None, appName=None, streamName=None, date=None, total=None):
        """
        :param publishDomain: (Optional) 查询的推流域名
        :param appName: (Optional) 查询的应用名称
        :param streamName: (Optional) 查询的流名
        :param date: (Optional) 日期:
  - yyyyMMdd 示例:20190308

        :param total: (Optional) 单日截图总张数:
  - 单位: 张

        """

        self.publishDomain = publishDomain
        self.appName = appName
        self.streamName = streamName
        self.date = date
        self.total = total
