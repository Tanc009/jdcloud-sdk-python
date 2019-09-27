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


class IpResourceInfo(object):

    def __init__(self, ip=None, safeStatus=None, region=None, blackHoleThreshold=None, cleanThresholdBps=None, cleanThresholdPps=None):
        """
        :param ip: (Optional) 公网 IP 地址
        :param safeStatus: (Optional) 安全状态, 0->安全, 1->清洗, 2->黑洞
        :param region: (Optional) 地域
        :param blackHoleThreshold: (Optional) 黑洞阈值, 单位 bps
        :param cleanThresholdBps: (Optional) 触发清洗的流量速率, 单位 bps
        :param cleanThresholdPps: (Optional) 触发清洗的包速率, 单位 pps
        """

        self.ip = ip
        self.safeStatus = safeStatus
        self.region = region
        self.blackHoleThreshold = blackHoleThreshold
        self.cleanThresholdBps = cleanThresholdBps
        self.cleanThresholdPps = cleanThresholdPps