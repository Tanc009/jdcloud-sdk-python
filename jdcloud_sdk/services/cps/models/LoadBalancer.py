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


class LoadBalancer(object):

    def __init__(self, loadBalancerId=None, region=None, ipAddressType=None, netType=None, vpcId=None, elasticIpId=None, publicIp=None, bandwidth=None, status=None, name=None, description=None, createTime=None, charge=None):
        """
        :param loadBalancerId: (Optional) 负载均衡实例ID
        :param region: (Optional) 地域，如cn-east-1
        :param ipAddressType: (Optional) IP版本，取值ipv4
        :param netType: (Optional) 网络类型，取值public
        :param vpcId: (Optional) 私有网络ID
        :param elasticIpId: (Optional) 弹性公网IPID
        :param publicIp: (Optional) 公网IP
        :param bandwidth: (Optional) 带宽
        :param status: (Optional) 状态，取值active|inactive
        :param name: (Optional) 名称
        :param description: (Optional) 描述
        :param createTime: (Optional) 创建时间
        :param charge: (Optional) 计费配置
        """

        self.loadBalancerId = loadBalancerId
        self.region = region
        self.ipAddressType = ipAddressType
        self.netType = netType
        self.vpcId = vpcId
        self.elasticIpId = elasticIpId
        self.publicIp = publicIp
        self.bandwidth = bandwidth
        self.status = status
        self.name = name
        self.description = description
        self.createTime = createTime
        self.charge = charge
