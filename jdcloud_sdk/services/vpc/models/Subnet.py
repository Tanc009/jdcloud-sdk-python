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


class Subnet(object):

    def __init__(self, subnetId=None, subnetName=None, vpcId=None, addressPrefix=None, availableIpCount=None, description=None, routeTableId=None, aclId=None, startIp=None, endIp=None, createdTime=None, subnetType=None, az=None):
        """
        :param subnetId: (Optional) Subnet的Id
        :param subnetName: (Optional) 子网名称
        :param vpcId: (Optional) 子网所属VPC的Id
        :param addressPrefix: (Optional) 子网网段，vpc内子网网段不能重叠，cidr的取值范围：10.0.0.0/8、172.16.0.0/12和192.168.0.0/16及它们包含的子网，且子网掩码长度为16-28之间，如果VPC含有Cidr，则必须为VPC所在Cidr的子网
        :param availableIpCount: (Optional) 子网可用ip数量
        :param description: (Optional) 子网描述信息
        :param routeTableId: (Optional) 子网关联的路由表Id
        :param aclId: (Optional) 子网关联的acl Id
        :param startIp: (Optional) 子网的起始地址，子网第1个地位为路由器网关保留，第2个地址为dhcp服务保留
        :param endIp: (Optional) 子网的结束地址，子网第1个地位为路由器网关保留，第2个地址为dhcp服务保留
        :param createdTime: (Optional) 子网创建时间
        :param subnetType: (Optional) 子网类型，取值：standard(标准子网)，edge(边缘子网)
        :param az: (Optional) 子网可用区
        """

        self.subnetId = subnetId
        self.subnetName = subnetName
        self.vpcId = vpcId
        self.addressPrefix = addressPrefix
        self.availableIpCount = availableIpCount
        self.description = description
        self.routeTableId = routeTableId
        self.aclId = aclId
        self.startIp = startIp
        self.endIp = endIp
        self.createdTime = createdTime
        self.subnetType = subnetType
        self.az = az
