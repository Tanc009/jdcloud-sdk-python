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


class DescribeDomainsLogRequest(JDCloudRequest):
    """
    日志下载
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeDomainsLogRequest, self).__init__(
            '/describeDomainsLog', 'GET', header, version)
        self.parameters = parameters


class DescribeDomainsLogParameters(object):

    def __init__(self, domains, startTime, ):
        """
        :param domains: 播放域名，多个时以逗号（,）分隔
        :param startTime: 起始时间
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z

        """

        self.domains = domains
        self.interval = None
        self.startTime = startTime
        self.endTime = None

    def setInterval(self, interval):
        """
        :param interval: (Optional) 时间间隔，取值(hour，day),不传默认小时
- 按小时（hour）下载时是.log文件
- 按天（day）下载时是.zip文件

        """
        self.interval = interval

    def setEndTime(self, endTime):
        """
        :param endTime: (Optional) 结束时间:
- UTC时间
  格式:yyyy-MM-dd'T'HH:mm:ss'Z'
  示例:2018-10-21T10:00:00Z
- 为空,默认为当前时间

        """
        self.endTime = endTime

