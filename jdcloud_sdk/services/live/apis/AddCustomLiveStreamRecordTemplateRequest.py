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


class AddCustomLiveStreamRecordTemplateRequest(JDCloudRequest):
    """
    添加录制模板
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddCustomLiveStreamRecordTemplateRequest, self).__init__(
            '/recordCustoms:template', 'POST', header, version)
        self.parameters = parameters


class AddCustomLiveStreamRecordTemplateParameters(object):

    def __init__(self, recordPeriod, saveBucket, saveEndpoint, recordFileType, template):
        """
        :param recordPeriod: 自动录制周期
        :param saveBucket: null
        :param saveEndpoint: null
        :param recordFileType: 录制文件格式
        :param template: 录制模板自定义名称
        """

        self.recordPeriod = recordPeriod
        self.saveBucket = saveBucket
        self.saveEndpoint = saveEndpoint
        self.recordFileType = recordFileType
        self.template = template

