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


class ProtectionOutline(object):

    def __init__(self, protectedDay=None, protectedIpCount=None, weekAttackCount=None, weekAttackPeak=None, weekAttackUnit=None, monthAttackCount=None, monthAttackPeak=None, monthAttackUnit=None, currentAttackCount=None):
        """
        :param protectedDay: (Optional) 已防护天数
        :param protectedIpCount: (Optional) 已防护 IP 数量
        :param weekAttackCount: (Optional) 7 日攻击次数
        :param weekAttackPeak: (Optional) 7 日攻击流量峰值
        :param weekAttackUnit: (Optional) 7 日攻击流量单位
        :param monthAttackCount: (Optional) 30 日攻击次数
        :param monthAttackPeak: (Optional) 30 日攻击流量峰值
        :param monthAttackUnit: (Optional) 30 日攻击流量单位
        :param currentAttackCount: (Optional) 当前攻击数量
        """

        self.protectedDay = protectedDay
        self.protectedIpCount = protectedIpCount
        self.weekAttackCount = weekAttackCount
        self.weekAttackPeak = weekAttackPeak
        self.weekAttackUnit = weekAttackUnit
        self.monthAttackCount = monthAttackCount
        self.monthAttackPeak = monthAttackPeak
        self.monthAttackUnit = monthAttackUnit
        self.currentAttackCount = currentAttackCount