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


class SkipActionCfg(object):

    def __init__(self, passAll, cc, waf, deny, rateLimit, bot, risk, ):
        """
        :param passAll:  是否跳过所有阶段，1表示是，0表示否
        :param cc:  是否执行cc防护，1表示是，0表示否
        :param waf:  是否执行waf防护，1表示是，0表示否
        :param deny:  是否执行deny防护，1表示是，0表示否
        :param rateLimit:  是否执行限速，1表示是，0表示否
        :param bot:  是否执行bot，1表示是，0表示否
        :param risk:  是否执行风控，1表示是，0表示否
        """

        self.passAll = passAll
        self.cc = cc
        self.waf = waf
        self.deny = deny
        self.rateLimit = rateLimit
        self.bot = bot
        self.risk = risk
