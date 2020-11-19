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


class CreateReadWriteProxyRequest(JDCloudRequest):
    """
    创建数据库读写分离代理服务<br>- 仅支持MySQL
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateReadWriteProxyRequest, self).__init__(
            '/regions/{regionId}/readWriteProxy', 'POST', header, version)
        self.parameters = parameters


class CreateReadWriteProxyParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.delayThreshold = None
        self.loadBalancerPolicy = None
        self.healthCheckSpec = None

    def setDelayThreshold(self, delayThreshold):
        """
        :param delayThreshold: (Optional) 延迟阈值，范围是0~1000，单位：秒，默认为100
        """
        self.delayThreshold = delayThreshold

    def setLoadBalancerPolicy(self, loadBalancerPolicy):
        """
        :param loadBalancerPolicy: (Optional) 读写分离代理后端实例负载均衡策略，默认值为LEAST_CURRENT_OPERATIONS；当前支持的负载均衡策略请查看[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        """
        self.loadBalancerPolicy = loadBalancerPolicy

    def setHealthCheckSpec(self, healthCheckSpec):
        """
        :param healthCheckSpec: (Optional) 后端实例健康检查配置
        """
        self.healthCheckSpec = healthCheckSpec
