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


class AddLiveStreamAppSnapshotRequest(JDCloudRequest):
    """
    添加app直播截图配置
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(AddLiveStreamAppSnapshotRequest, self).__init__(
            '/snapshotApps:template', 'POST', header, version)
        self.parameters = parameters


class AddLiveStreamAppSnapshotParameters(object):

    def __init__(self, appName, publishDomain, template):
        """
        :param appName: 直播流所属应用名称
        :param publishDomain: 您的推流加速域名
        :param template: 截图模版
        """

        self.appName = appName
        self.publishDomain = publishDomain
        self.template = template

