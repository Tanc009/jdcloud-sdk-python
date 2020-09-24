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


class BandwidthPackage(object):

    def __init__(self, region=None, az=None, bandwidthPackageId=None, bandwidth=None, extraUplinkBandwidth=None, lineType=None, name=None, createTime=None, charge=None):
        """
        :param region: (Optional) 区域代码, 如cn-east-tz1
        :param az: (Optional) 可用区代码, 如cn-east-tz1a
        :param bandwidthPackageId: (Optional) 共享带宽ID
        :param bandwidth: (Optional) 带宽, 单位Mbps
        :param extraUplinkBandwidth: (Optional) 额外上行带宽, 单位Mbps
        :param lineType: (Optional) 链路类型
        :param name: (Optional) 名称
        :param createTime: (Optional) 创建时间
        :param charge: (Optional) 计费信息
        """

        self.region = region
        self.az = az
        self.bandwidthPackageId = bandwidthPackageId
        self.bandwidth = bandwidth
        self.extraUplinkBandwidth = extraUplinkBandwidth
        self.lineType = lineType
        self.name = name
        self.createTime = createTime
        self.charge = charge
