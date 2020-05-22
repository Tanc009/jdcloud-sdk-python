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


class ListProductsWithAdminRequest(JDCloudRequest):
    """
    查看所有产品的列表
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(ListProductsWithAdminRequest, self).__init__(
            '/regions/{regionId}/loongrayinstances/{instanceId}/products:describeAll', 'GET', header, version)
        self.parameters = parameters


class ListProductsWithAdminParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域ID
        :param instanceId: IoT Engine实例ID信息
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.pageNumber = None
        self.pageSize = None
        self.filters = None

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码, 默认为1, 取值范围：[1,∞)
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小，默认为10，取值范围：[10,100]
        """
        self.pageSize = pageSize

    def setFilters(self, filters):
        """
        :param filters: (Optional) productName-产品名称，模糊匹配，支持单个
productKey-产品key，精确匹配，支持单个
productType-产品类型，精确匹配，支持单个
templateName-模板名称，精确匹配，支持多个

        """
        self.filters = filters

