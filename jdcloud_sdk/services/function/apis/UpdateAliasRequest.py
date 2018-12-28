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


class UpdateAliasRequest(JDCloudRequest):
    """
    更新别名
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateAliasRequest, self).__init__(
            '/regions/{regionId}/functions/{functionName}/aliases/{aliasName}', 'PUT', header, version)
        self.parameters = parameters


class UpdateAliasParameters(object):

    def __init__(self, regionId, functionName, aliasName, description, version):
        """
        :param regionId: Region ID
        :param functionName: 别名所属函数名称
        :param aliasName: 别名名称
        :param description: 别名描述信息
        :param version: 别名对应版本
        """

        self.regionId = regionId
        self.functionName = functionName
        self.aliasName = aliasName
        self.description = description
        self.version = version

