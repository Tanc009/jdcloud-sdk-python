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


class LoadBalancerSpec(object):

    def __init__(self, netType, ipAddressType, vpcId, name, applyElasticIp, bandwidth, charge, description=None):
        """
        :param netType:  网络类型，取值public
        :param ipAddressType:  负载均衡实例的IP版本，取值ipv4
        :param vpcId:  私有网络ID
        :param name:  名称
        :param description: (Optional) 描述
        :param applyElasticIp:  是否申请弹性公网Ip
        :param bandwidth:  带宽
        :param charge:  计费配置
        """

        self.netType = netType
        self.ipAddressType = ipAddressType
        self.vpcId = vpcId
        self.name = name
        self.description = description
        self.applyElasticIp = applyElasticIp
        self.bandwidth = bandwidth
        self.charge = charge
