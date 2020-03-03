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


class CreateTranscodeTemplateRequest(JDCloudRequest):
    """
    创建转码模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateTranscodeTemplateRequest, self).__init__(
            '/transcodeTemplates', 'POST', header, version)
        self.parameters = parameters


class CreateTranscodeTemplateParameters(object):

    def __init__(self, title, video, audio, container, definition, ):
        """
        :param title: 模板标题。长度不超过 128 个字符，最少 2 个字符。UTF-8 编码。

        :param video: 视频参数配置
        :param audio: 音频参数配置
        :param container: 容器封装配置
        :param definition: 清晰度规格标记。取值范围：
  SD - 标清
  HD - 高清
  FHD - 超清
  2K
  4K

        """

        self.title = title
        self.video = video
        self.audio = audio
        self.container = container
        self.encryption = None
        self.definition = definition
        self.transcodeType = None

    def setEncryption(self, encryption):
        """
        :param encryption: (Optional) 加密配置
        """
        self.encryption = encryption

    def setTranscodeType(self, transcodeType):
        """
        :param transcodeType: (Optional) 转码方式。取值范围：
  normal - 普通转码
  jdchd - 京享超清
  jdchs - 极速转码
默认值为 normal

        """
        self.transcodeType = transcodeType

