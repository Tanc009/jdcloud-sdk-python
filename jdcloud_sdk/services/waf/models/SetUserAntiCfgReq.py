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


class SetUserAntiCfgReq(object):

    def __init__(self, wafInstanceId, domain, filterHeaderEnable=None, reqHeaderEnable=None, respHeaderEnable=None, filterSenseEnable=None, statusEnable=None, skipEnable=None, denyEnable=None, ratelimitEnable=None, uriRewriteEnable=None):
        """
        :param wafInstanceId:  WAF实例id
        :param domain:  域名
        :param filterHeaderEnable: (Optional) 是否开启头管理，"1"表示使能,"0"表示否，即将废弃
        :param reqHeaderEnable: (Optional) 是否开启请求头管理，"1"表示使能,"0"表示否
        :param respHeaderEnable: (Optional) 是否开启响应头管理，"1"表示使能,"0"表示否
        :param filterSenseEnable: (Optional) 是否开启敏感信息防泄漏，"1"表示使能,"0"表示否
        :param statusEnable: (Optional) 是否开启状态码修改，"1"表示使能,"0"表示否
        :param skipEnable: (Optional) 是否开启白名单，"1"表示使能,"0"表示否
        :param denyEnable: (Optional) 是否开启黑名单，"1"表示使能,"0"表示否
        :param ratelimitEnable: (Optional) 是否开启限速，"1"表示使能,"0"表示否
        :param uriRewriteEnable: (Optional) 是否开启uri重写，"1"表示使能,"0"表示否
        """

        self.wafInstanceId = wafInstanceId
        self.domain = domain
        self.filterHeaderEnable = filterHeaderEnable
        self.reqHeaderEnable = reqHeaderEnable
        self.respHeaderEnable = respHeaderEnable
        self.filterSenseEnable = filterSenseEnable
        self.statusEnable = statusEnable
        self.skipEnable = skipEnable
        self.denyEnable = denyEnable
        self.ratelimitEnable = ratelimitEnable
        self.uriRewriteEnable = uriRewriteEnable
