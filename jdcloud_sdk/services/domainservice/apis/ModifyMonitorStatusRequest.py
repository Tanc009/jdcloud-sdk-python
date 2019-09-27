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


class ModifyMonitorStatusRequest(JDCloudRequest):
    """
    监控项的操作集合，包括：暂停，启动, 手动恢复, 手动切换
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(ModifyMonitorStatusRequest, self).__init__(
            '/regions/{regionId}/domain/{domainId}/monitor/{monitorId}/status', 'PUT', header, version)
        self.parameters = parameters


class ModifyMonitorStatusParameters(object):

    def __init__(self, regionId, domainId, monitorId, action, ):
        """
        :param regionId: 实例所属的地域ID
        :param domainId: 域名ID，请使用describeDomains接口获取。
        :param monitorId: 监控项ID，请使用describeMonitor接口获取。
        :param action: 暂停stop, 开启start, 手动恢复recover，手动切换switch，手动恢复和手动切换时候不支持批量操作
        """

        self.regionId = regionId
        self.domainId = domainId
        self.monitorId = monitorId
        self.action = action
        self.switchTarget = None

    def setSwitchTarget(self, switchTarget):
        """
        :param switchTarget: (Optional) 监控项的主机值, 手动切换时必填
        """
        self.switchTarget = switchTarget
