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


class AuditConfig(object):

    def __init__(self, agentId=None, auditSpec=None, netCard=None):
        """
        :param agentId: (Optional) agentID列表
        :param auditSpec: (Optional) 实例配置信息
        :param netCard: (Optional) 网卡列表
        """

        self.agentId = agentId
        self.auditSpec = auditSpec
        self.netCard = netCard
