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


class CreateInstanceFromBackupRequest(JDCloudRequest):
    """
    根据源实例全量备份创建一个新实例，新实例的数据跟源实例在创建备份时的数据状态一样。<br>例如根据源实例A的一个全量备份“mybak”新建一个实例B，该备份是在“‘2018-8-18 03:23:54”创建的。那么新建实例B的数据状态跟实例A‘2018-8-18 03:23:54’的状态一致
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateInstanceFromBackupRequest, self).__init__(
            '/regions/{regionId}/instances:createInstanceFromBackup', 'POST', header, version)
        self.parameters = parameters


class CreateInstanceFromBackupParameters(object):

    def __init__(self, regionId, backupId, engine, instanceSpec):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param backupId: 备份ID
        :param engine: 标识是创建什么类型的实例，例如MySQL，SQL Server等,具体可参见文档[枚举参数定义](../Enum-Definitions/Enum-Definitions.md)<br>**注意：备份来源实例的engine和要创建的实例的engine必须一致**
        :param instanceSpec: 新建实例规格
        """

        self.regionId = regionId
        self.backupId = backupId
        self.engine = engine
        self.instanceSpec = instanceSpec

