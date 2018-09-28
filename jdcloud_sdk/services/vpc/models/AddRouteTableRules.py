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


class AddRouteTableRules(object):

    def __init__(self, nextHopType, nextHopId, addressPrefix, priority=None):
        """
        :param nextHopType:  下一跳类型, 取值范围:instance:云主机, internet:公网, vpc_peering:vpc对等连接, bgw:边界网关
        :param nextHopId:  下一跳id
        :param addressPrefix:  匹配地址前缀, internet类型路由跟其他类型的路由，addressPrefix不允许重复
        :param priority: (Optional) 规则匹配优先级，取值范围[1,255]，默认为100。当路由规则子网掩码不同时，路由最长匹配优先；当路由规则子网掩码相同时, 按照优先级匹配转发, 优先级数字越小优先级越高，路由规则子网掩码相同、优先级相同、下一跳不同时，形成等价路由，不同下一跳负载均担。
        """

        self.nextHopType = nextHopType
        self.nextHopId = nextHopId
        self.addressPrefix = addressPrefix
        self.priority = priority