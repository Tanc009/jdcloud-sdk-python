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


class DescribeTargetGroupsRequest(JDCloudRequest):
    """
    查询虚拟服务器组列表详情，返回target详情功能3个月后将会下线，建议用户直接使用describeTargets接口查询target详情
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeTargetGroupsRequest, self).__init__(
            '/regions/{regionId}/targetGroups/', 'GET', header, version)
        self.parameters = parameters


class DescribeTargetGroupsParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: Region ID
        """

        self.regionId = regionId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞), 页码超过总页数时, 显示最后一页
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为20，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) targetGroupIds - TargetGroup ID列表，支持多个
targetGroupNames - TargetGroup名称列表，支持多个
loadBalancerId － TargetGroup所属负载均衡的Id，支持单个
loadBalancerType - 负载均衡类型，取值为：alb、nlb、dnlb，默认alb，支持单个

        """
        self.filters = filters

