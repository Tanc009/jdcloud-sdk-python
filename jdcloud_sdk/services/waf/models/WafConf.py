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


class WafConf(object):

    def __init__(self, enable=None, wafMode=None, wafLevel=None, redirection=None):
        """
        :param enable: (Optional) 是否使能 0表示否
        :param wafMode: (Optional) 0表示防护，1表示预警
        :param wafLevel: (Optional) 0表示宽松，1表示正常，2表示严格
        :param redirection: (Optional) 自定义页面名称
        """

        self.enable = enable
        self.wafMode = wafMode
        self.wafLevel = wafLevel
        self.redirection = redirection
