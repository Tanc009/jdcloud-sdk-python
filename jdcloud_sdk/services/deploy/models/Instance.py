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


class Instance(object):

    def __init__(self, instanceId=None, uuid=None, instanceName=None, ip=None, public_ip=None, regionId=None, vpc=None, type=None, ag=None, tags=None, groupId=None, agentStatus=None):
        """
        :param instanceId: (Optional) 云主机ID
        :param uuid: (Optional) 云主机ID
        :param instanceName: (Optional) 云主机名称
        :param ip: (Optional) ip
        :param public_ip: (Optional) 公网ip
        :param regionId: (Optional) 地域
        :param vpc: (Optional) 私有网络
        :param type: (Optional) 类型 1云主机，2原生容器
        :param ag: (Optional) 高可用组
        :param tags: (Optional) 标签
        :param groupId: (Optional) 所属部署组ID，多个,分隔
        :param agentStatus: (Optional) 客户端状态
        """

        self.instanceId = instanceId
        self.uuid = uuid
        self.instanceName = instanceName
        self.ip = ip
        self.public_ip = public_ip
        self.regionId = regionId
        self.vpc = vpc
        self.type = type
        self.ag = ag
        self.tags = tags
        self.groupId = groupId
        self.agentStatus = agentStatus
