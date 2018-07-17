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


class InstanceTemplateElasticIpSpec(object):

    def __init__(self, bandwidthMbps, chargeMode, provider=None):
        """
        :param bandwidthMbps:  弹性公网IP的限速（单位：MB）
        :param provider: (Optional) IP服务商，取值为BGP,nonBGP
        :param chargeMode:  计费类型，bandwith，flow
        """

        self.bandwidthMbps = bandwidthMbps
        self.provider = provider
        self.chargeMode = chargeMode
