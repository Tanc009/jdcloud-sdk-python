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


class TrafficSamplingData(object):

    def __init__(self, srcIp=None, dstIp=None, srcPort=None, dstPort=None, sampleDataLength=None, samplingInterval=None, protocolName=None, timestamp=None, uniqueId=None, operatorType=None):
        """
        :param srcIp: (Optional) 源IP
        :param dstIp: (Optional) 目的IP
        :param srcPort: (Optional) 源端口
        :param dstPort: (Optional) 目的端口
        :param sampleDataLength: (Optional) 采样包长度
        :param samplingInterval: (Optional) 采样比
        :param protocolName: (Optional) 协议
        :param timestamp: (Optional) 时间戳
        :param uniqueId: (Optional) 唯一ID标识
        :param operatorType: (Optional) 运营商类型 移动:CM 联通:CU 电信:CT
        """

        self.srcIp = srcIp
        self.dstIp = dstIp
        self.srcPort = srcPort
        self.dstPort = dstPort
        self.sampleDataLength = sampleDataLength
        self.samplingInterval = samplingInterval
        self.protocolName = protocolName
        self.timestamp = timestamp
        self.uniqueId = uniqueId
        self.operatorType = operatorType
