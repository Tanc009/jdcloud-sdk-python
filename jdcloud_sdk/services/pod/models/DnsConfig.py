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


class DnsConfig(object):

    def __init__(self, nameservers=None, searches=None, options=None):
        """
        :param nameservers: (Optional) DNS服务器IP地址列表。

        :param searches: (Optional) DNS搜索域列表，用于主机名查找。

        :param options: (Optional) DNS解析器选项列表。
        """

        self.nameservers = nameservers
        self.searches = searches
        self.options = options
