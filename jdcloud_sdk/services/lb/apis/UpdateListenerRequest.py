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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class UpdateListenerRequest(JDCloudRequest):
    """
    修改一个监听器的信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateListenerRequest, self).__init__(
            '/regions/{regionId}/listeners/{listenerId}', 'PATCH', header, version)
        self.parameters = parameters


class UpdateListenerParameters(object):

    def __init__(self, regionId, listenerId, ):
        """
        :param regionId: Region ID
        :param listenerId: 监听器ID
        """

        self.regionId = regionId
        self.listenerId = listenerId
        self.listenerName = None
        self.status = None
        self.certificateSpecs = None
        self.connectionIdleTimeSeconds = None
        self.backendId = None
        self.urlMapId = None
        self.description = None

    def setListenerName(self, listenerName):
        """
        :param listenerName: (Optional) 监听器名称,只允许输入中文、数字、大小写字母、英文下划线“_”及中划线“-”，不允许为空且不超过32字符
        """
        self.listenerName = listenerName

    def setStatus(self, status):
        """
        :param status: (Optional) Listener状态, 取值为On或者为Off
        """
        self.status = status

    def setCertificateSpecs(self, certificateSpecs):
        """
        :param certificateSpecs: (Optional) 【alb Https和Tls协议】ssl server证书列表，现只支持一个证书
        """
        self.certificateSpecs = certificateSpecs

    def setConnectionIdleTimeSeconds(self, connectionIdleTimeSeconds):
        """
        :param connectionIdleTimeSeconds: (Optional) 【alb、nlb】空闲连接超时时间, 范围为[1,86400]。 <br>（Tcp和Tls协议）默认为：1800s <br>（Http和Https协议）默认为：60s <br>【dnlb】不支持该功能
        """
        self.connectionIdleTimeSeconds = connectionIdleTimeSeconds

    def setBackendId(self, backendId):
        """
        :param backendId: (Optional) 默认后端服务Id
        """
        self.backendId = backendId

    def setUrlMapId(self, urlMapId):
        """
        :param urlMapId: (Optional) 【alb Https和Http协议】转发规则组Id
        """
        self.urlMapId = urlMapId

    def setDescription(self, description):
        """
        :param description: (Optional) 监听器描述,允许输入UTF-8编码下的全部字符，不超过256字符
        """
        self.description = description
