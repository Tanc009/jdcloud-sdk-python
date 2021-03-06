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


class GetTaskInfoByIdRequest(JDCloudRequest):
    """
    读取指定ID的运行结果和运行状态
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(GetTaskInfoByIdRequest, self).__init__(
            '/regions/{regionId}/task_infos/{task}', 'GET', header, version)
        self.parameters = parameters


class GetTaskInfoByIdParameters(object):

    def __init__(self, regionId, task, ):
        """
        :param regionId: 地域ID
        :param task: 执行请求 ID
        """

        self.regionId = regionId
        self.task = task
        self.fileName = None

    def setFileName(self, fileName):
        """
        :param fileName: (Optional) 执行文件名称
        """
        self.fileName = fileName

