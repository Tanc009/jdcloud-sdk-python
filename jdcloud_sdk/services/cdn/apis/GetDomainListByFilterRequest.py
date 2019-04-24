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


class GetDomainListByFilterRequest(JDCloudRequest):
    """
    通过标签查询加速域名接口
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetDomainListByFilterRequest, self).__init__(
            '/domain:query', 'POST', header, version)
        self.parameters = parameters


class GetDomainListByFilterParameters(object):

    def __init__(self, ):
        """
        """

        self.keyWord = None
        self.pageNumber = None
        self.pageSize = None
        self.status = None
        self.type = None
        self.tagFilters = None

    def setKeyWord(self, keyWord):
        """
        :param keyWord: (Optional) 根据关键字进行模糊匹配
        """
        self.keyWord = keyWord

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) pageNumber
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) pageSize
        """
        self.pageSize = pageSize

    def setStatus(self, status):
        """
        :param status: (Optional) 根据域名状态查询, 可选值[offline, online, configuring, auditing, audit_reject]
        """
        self.status = status

    def setType(self, type):
        """
        :param type: (Optional) type
        """
        self.type = type

    def setTagFilters(self, tagFilters):
        """
        :param tagFilters: (Optional) 标签过滤条件
        """
        self.tagFilters = tagFilters
