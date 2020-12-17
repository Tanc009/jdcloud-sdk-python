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


class QueryCustomizedDirBandWidthRequest(JDCloudRequest):
    """
    查询定制的目录带宽，仅有部分用户支持该功能
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QueryCustomizedDirBandWidthRequest, self).__init__(
            '/statistics:queryCustomizedDirBandWidth', 'POST', header, version)
        self.parameters = parameters


class QueryCustomizedDirBandWidthParameters(object):

    def __init__(self, ):
        """
        """

        self.startTime = None
        self.endTime = None
        self.domain = None
        self.dir = None

    def setStartTime(self, startTime):
        """
        :param startTime: (Optional) 查询起始时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2020-12-07T16:00:00Z
        """
        self.startTime = startTime

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 查询截止时间,UTC时间，格式为:yyyy-MM-dd'T'HH:mm:ss'Z'，示例:2020-12-07T16:20:00Z，开始时间和结束时间跨度 不能超过4个小时
        """
        self.endTime = endTime

    def setDomain(self, domain):
        """
        :param domain: (Optional) 需要查询的域名, 必须为用户pin下有权限的域名，该接口仅支持单域名查询
        """
        self.domain = domain

    def setDir(self, dir):
        """
        :param dir: (Optional) 需要过滤的目录，以正斜线(/)开头，不填表示查询所有目录。查询目录同时需要以正斜线(/)结尾。 如:/path1/path2/path3/
        """
        self.dir = dir

