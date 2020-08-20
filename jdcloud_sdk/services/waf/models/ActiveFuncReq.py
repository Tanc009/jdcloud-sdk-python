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


class ActiveFuncReq(object):

    def __init__(self, domain, wafInstanceId=None, enable=None):
        """
        :param wafInstanceId: (Optional) 实例id，代表要设置的WAF实例
        :param domain:  域名
        :param enable: (Optional) 是否使能 0表示否
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.enable = enable
