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


class DeleteRuleGroupRequest(JDCloudRequest):
    """
    删除规则组
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DeleteRuleGroupRequest, self).__init__(
            '/regions/{regionId}/instances/{insId}/ruleGroups/{ruleGroupId}', 'DELETE', header, version)
        self.parameters = parameters


class DeleteRuleGroupParameters(object):

    def __init__(self, regionId, insId, ruleGroupId, ):
        """
        :param regionId: 地域 Id
        :param insId: 审计实例ID
        :param ruleGroupId: 规则组ID
        """

        self.regionId = regionId
        self.insId = insId
        self.ruleGroupId = ruleGroupId
        self.dbId = None

    def setDbId(self, dbId):
        """
        :param dbId: (Optional) 数据库ID
        """
        self.dbId = dbId

