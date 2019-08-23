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


class CreateSuperAccountRequest(JDCloudRequest):
    """
    创建数据库账号，用户可以使用客户端，应用程序等通过该账号和密码登录RDS数据库实例。<br>为便于管理和恢复，RDS对账号进行了限制，数据库账号只能通过控制台或者OpenAPI进行创建、删除账号以及对账号授权等，用户不能通过SQL语句对账号进行相关操作。
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateSuperAccountRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/accounts:createSuperAccount', 'POST', header, version)
        self.parameters = parameters


class CreateSuperAccountParameters(object):

    def __init__(self, regionId, instanceId, accountName, accountPassword):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        :param accountName: 账号名，在同一个RDS实例中，账号名不能重复。账号名的具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param accountPassword: 密码,密码的具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.accountName = accountName
        self.accountPassword = accountPassword

