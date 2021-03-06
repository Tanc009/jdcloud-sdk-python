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


class ResourceEnd(object):

    def __init__(self, agentStatus=None, name=None, region=None, resourceId=None):
        """
        :param agentStatus: (Optional) agent 状态: 0-异常，1-正常
        :param name: (Optional) 资源名称
        :param region: (Optional) 资源所属地域
        :param resourceId: (Optional) 资源ID
        """

        self.agentStatus = agentStatus
        self.name = name
        self.region = region
        self.resourceId = resourceId
