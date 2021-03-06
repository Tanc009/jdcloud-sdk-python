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


class DeployRequest(JDCloudRequest):
    """
    发布版本
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeployRequest, self).__init__(
            '/regions/{regionId}/apiGroups/{apiGroupId}/deployments', 'POST', header, version)
        self.parameters = parameters


class DeployParameters(object):

    def __init__(self, regionId, apiGroupId, revision, environment, ):
        """
        :param regionId: 地域ID
        :param apiGroupId: 分组ID
        :param revision: 发布的修订版本号
        :param environment: 环境：test、preview、online
        """

        self.regionId = regionId
        self.apiGroupId = apiGroupId
        self.revision = revision
        self.environment = environment
        self.backendServiceType = None
        self.backendUrl = None
        self.description = None
        self.jdsfName = None
        self.jdsfRegistryName = None
        self.jdsfId = None

    def setBackendServiceType(self, backendServiceType):
        """
        :param backendServiceType: (Optional) 后端服务类型：mock、unique、vpc
        """
        self.backendServiceType = backendServiceType

    def setBackendUrl(self, backendUrl):
        """
        :param backendUrl: (Optional) 后端地址
        """
        self.backendUrl = backendUrl

    def setDescription(self, description):
        """
        :param description: (Optional) 描述
        """
        self.description = description

    def setJdsfName(self, jdsfName):
        """
        :param jdsfName: (Optional) 微服务网关名称
        """
        self.jdsfName = jdsfName

    def setJdsfRegistryName(self, jdsfRegistryName):
        """
        :param jdsfRegistryName: (Optional) 微服务注册中心ID
        """
        self.jdsfRegistryName = jdsfRegistryName

    def setJdsfId(self, jdsfId):
        """
        :param jdsfId: (Optional) 微服务ID
        """
        self.jdsfId = jdsfId

