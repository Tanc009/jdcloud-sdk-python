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


class LbConf(object):

    def __init__(self, protocols, lbType, sslProtocols=None, rsConfig=None, pureClient=None, httpsRedirect=None, rsOnlySupportHttp=None, httpsCertUpdateStatus=None, httpStatus=None, httpVersion=None, enableKeepalive=None, suiteLevel=None, enableUnderscores=None, maxBodySize=None):
        """
        :param protocols:  使用协议，["http","https"]
        :param sslProtocols: (Optional) ssl协议，eg:["TLSv1","TLSv1.1","TLSv1.2","SSLv2","SSLv3"]
        :param lbType:  负载均衡算法，eg:"rr"，"ip_hash"
        :param rsConfig: (Optional) 网站回源配置
        :param pureClient: (Optional) 是否使用前置代理，0为未使用，1为使用
        :param httpsRedirect: (Optional) 1为跳转 0为不跳转
        :param rsOnlySupportHttp: (Optional) 用户服务器是否只能http回源，1为是，0为否
        :param httpsCertUpdateStatus: (Optional) https证书状态,非配置项。-10为未绑定，0为已绑定
        :param httpStatus: (Optional) 协议状态,非配置项。0为正常，-10为不正常
        :param httpVersion: (Optional) Waf侧支持http版本，""为默认值http1.1,"http2"为http2
        :param enableKeepalive: (Optional) 回源是否支持长链接，0为否
        :param suiteLevel: (Optional) 加密套件等级，0表示默认为中级，1表示高级，2表示低级
        :param enableUnderscores: (Optional) 请求头是否支持下划线，1-是，0-否
        :param maxBodySize: (Optional) 请求body最大值，默认300M，可为G/K
        """

        self.protocols = protocols
        self.sslProtocols = sslProtocols
        self.lbType = lbType
        self.rsConfig = rsConfig
        self.pureClient = pureClient
        self.httpsRedirect = httpsRedirect
        self.rsOnlySupportHttp = rsOnlySupportHttp
        self.httpsCertUpdateStatus = httpsCertUpdateStatus
        self.httpStatus = httpStatus
        self.httpVersion = httpVersion
        self.enableKeepalive = enableKeepalive
        self.suiteLevel = suiteLevel
        self.enableUnderscores = enableUnderscores
        self.maxBodySize = maxBodySize
