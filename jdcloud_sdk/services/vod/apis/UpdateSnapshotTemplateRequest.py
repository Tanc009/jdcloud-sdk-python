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


class UpdateSnapshotTemplateRequest(JDCloudRequest):
    """
    修改截图模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(UpdateSnapshotTemplateRequest, self).__init__(
            '/snapshotTemplates/{templateId}', 'PATCH', header, version)
        self.parameters = parameters


class UpdateSnapshotTemplateParameters(object):

    def __init__(self, templateId, ):
        """
        :param templateId: 模板ID
        """

        self.templateId = templateId
        self.templateName = None
        self.templateConfig = None

    def setTemplateName(self, templateName):
        """
        :param templateName: (Optional) 模板名称
        """
        self.templateName = templateName

    def setTemplateConfig(self, templateConfig):
        """
        :param templateConfig: (Optional) 模板配置，JSON格式的字符串
        """
        self.templateConfig = templateConfig

