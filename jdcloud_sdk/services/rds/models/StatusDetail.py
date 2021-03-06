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


class StatusDetail(object):

    def __init__(self, instanceId=None, instanceName=None, instanceStatus=None, tdeStatus=None):
        """
        :param instanceId: (Optional) 实例ID
        :param instanceName: (Optional) 实例名称，具体规则可参见帮助中心文档:[名称及密码限制](../../../documentation/Database-and-Cache-Service/RDS/Introduction/Restrictions/SQLServer-Restrictions.md)
        :param instanceStatus: (Optional) 实例状态，参见[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)
        :param tdeStatus: (Optional) 开启TDE加密后，实例级别的TDE生效状态，TDE加密已生效，返回true；如未生效，返回false；
        """

        self.instanceId = instanceId
        self.instanceName = instanceName
        self.instanceStatus = instanceStatus
        self.tdeStatus = tdeStatus
