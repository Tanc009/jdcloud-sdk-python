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


class DeploymentAssociateEip(object):

    def __init__(self, eipId=None, instanceId=None, instanceType=None):
        """
        :param eipId: (Optional) 公网IP id
        :param instanceId: (Optional) 云产品的实例ID
        :param instanceType: (Optional) 要解绑的资源类型  虚拟机：vm 负载均衡：slb
        """

        self.eipId = eipId
        self.instanceId = instanceId
        self.instanceType = instanceType
