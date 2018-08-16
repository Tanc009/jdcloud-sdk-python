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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ModifyInstanceRequest(JDCloudRequest):
    """
    修改云物理服务器部分信息，包括名称、描述
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyInstance', 'POST', header, version)
        self.parameters = parameters


class ModifyInstanceParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID，可调用接口（describeRegiones）获取云物理服务器支持的地域
        :param instanceId: 云物理服务器ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.name = None
        self.description = None

    def setName(self, name):
        """
        :param name: (Optional) 云物理服务器名称
        """
        self.name = name

    def setDescription(self, description):
        """
        :param description: (Optional) 云物理服务器描述
        """
        self.description = description

