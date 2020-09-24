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


class DescribeClientIpDetailRequest(JDCloudRequest):
    """
    查询指定客户端IP的连接详细信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeClientIpDetailRequest, self).__init__(
            '/regions/{regionId}/cacheInstance/{cacheInstanceId}/clientIpDetail', 'POST', header, version)
        self.parameters = parameters


class DescribeClientIpDetailParameters(object):

    def __init__(self, regionId, cacheInstanceId, ip):
        """
        :param regionId: 缓存Redis实例所在区域的Region ID。目前有华北-北京、华南-广州、华东-上海三个区域，Region ID分别为cn-north-1、cn-south-1、cn-east-2
        :param cacheInstanceId: 缓存Redis实例ID，是访问实例的唯一标识
        :param ip: 客户端IP
        """

        self.regionId = regionId
        self.cacheInstanceId = cacheInstanceId
        self.ip = ip

