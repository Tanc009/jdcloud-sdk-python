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


class Segment(object):

    def __init__(self, segmentId=None, segmentName=None, description=None, addressPrefix=None, availableIpCount=None, provider=None, startIp=None, endIp=None):
        """
        :param segmentId: (Optional) 网段的Id
        :param segmentName: (Optional) 网段名称，只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符。
        :param description: (Optional) 网段描述，允许输入UTF-8编码下的全部字符，不超过256字符。
        :param addressPrefix: (Optional) 网络地址段
        :param availableIpCount: (Optional) 网段可用ip数量
        :param provider: (Optional) IP服务商，取值为bgp或no_bgp，cn-north-1：bgp；cn-south-1：bgp；cn-east-1：bgp；cn-east-2：bgp
        :param startIp: (Optional) 网段的起始地址
        :param endIp: (Optional) 网段的结束地址
        """

        self.segmentId = segmentId
        self.segmentName = segmentName
        self.description = description
        self.addressPrefix = addressPrefix
        self.availableIpCount = availableIpCount
        self.provider = provider
        self.startIp = startIp
        self.endIp = endIp
