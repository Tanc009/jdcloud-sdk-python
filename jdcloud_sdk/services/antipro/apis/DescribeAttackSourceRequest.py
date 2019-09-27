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


class DescribeAttackSourceRequest(JDCloudRequest):
    """
    查询攻击来源
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DescribeAttackSourceRequest, self).__init__(
            '/attacklog/{attackLogId}:describeAttackSource', 'GET', header, version)
        self.parameters = parameters


class DescribeAttackSourceParameters(object):

    def __init__(self, attackLogId, ip):
        """
        :param attackLogId: 攻击记录 Id
        :param ip: DDoS 防护包已防护的公网 IP
- 使用 <a href="http://docs.jdcloud.com/anti-ddos-protection-package/api/describeprotectediplist">describeProtectedIpList</a> 接口查询 DDoS 防护包已防护的公网 IP

        """

        self.attackLogId = attackLogId
        self.ip = ip
