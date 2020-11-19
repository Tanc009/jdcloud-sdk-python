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


class DescribeInstancesInternalRequest(JDCloudRequest):
    """
    获取当前账号下所有 RDS 实例及 MySQL /PostgreSQL 只读实例的概要信息，不会返回计费相关信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeInstancesInternalRequest, self).__init__(
            '/regions/{regionId}/instances:describeInstancesInternal', 'GET', header, version)
        self.parameters = parameters


class DescribeInstancesInternalParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 显示数据的页码，默认为1，取值范围：[-1,∞)。pageNumber为-1时，返回所有数据页码；超过总页数时，显示最后一页;
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 每页显示的数据条数，默认为100，取值范围：[10,100]，用于查询列表的接口
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) 过滤参数，多个过滤参数之间的关系为“与”(and)
支持以下属性的过滤：
instanceId, 支持operator选项：eq
instanceName, 支持operator选项：eq
engine, 支持operator选项：eq
instanceType, 支持operator选项：eq
instanceStatus, 支持operator选项：eq

        """
        self.filters = filters
