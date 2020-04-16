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


class DescribeIpResourceProtectInfoRequest(JDCloudRequest):
    """
    查询公网 IP 的攻击记录, 仅支持 ipv4. (已废弃, 建议使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeattacklogs'>describeAttackLogs</a> 接口)

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeIpResourceProtectInfoRequest, self).__init__(
            '/regions/{regionId}/ipResources/{ip}/protectInfo', 'GET', header, version)
        self.parameters = parameters


class DescribeIpResourceProtectInfoParameters(object):

    def __init__(self, regionId, ip, ):
        """
        :param regionId: 地域编码. 基础防护已支持华北-北京, 华东-宿迁, 华东-上海, 华南-广州
        :param ip: 基础防护已防护的公网 IP, 仅支持 ipv4 格式. <br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeelasticipresources'>describeElasticIpResources</a> 接口查询基础防护已防护的私有网络弹性公网 IP<br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describecpsipresources'>describeCpsIpResources</a> 接口查询基础防护已防护的云物理服务器公网 IP 和 弹性公网 IP<br>- 使用 <a href='http://docs.jdcloud.com/anti-ddos-basic/api/describeccsipresources'>describeCcsIpResources</a> 接口查询基础防护已防护的托管区公网 IP
        """

        self.regionId = regionId
        self.ip = ip
        self.start = None
        self.limit = None

    def setStart(self, start):
        """
        :param start: (Optional) 限制查询的开始范围
        """
        self.start = start

    def setLimit(self, limit):
        """
        :param limit: (Optional) 限制查询的记录数
        """
        self.limit = limit

