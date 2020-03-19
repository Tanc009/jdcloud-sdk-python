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


class CreateProductTopicRequest(JDCloudRequest):
    """
    新建产品自定义Topic
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(CreateProductTopicRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/products/{productKey}/topics', 'POST', header, version)
        self.parameters = parameters


class CreateProductTopicParameters(object):

    def __init__(self, regionId, instanceId, productKey, topicShortName, topicOperation, ):
        """
        :param regionId: 地域ID
        :param instanceId: IoTCore实例ID信息
        :param productKey: 产品Key
        :param topicShortName: Topic名称为必填，同一个产品下的Topic名称不能重复
只能包含字母，数字和下划线，最多64个字符，每个层级都不能为空
不能以/结尾

        :param topicOperation: 操作权限，设备对该Topic类的操作权限，取值
pub:发布
sub:订阅

        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.productKey = productKey
        self.topicShortName = topicShortName
        self.topicOperation = topicOperation
        self.topicDescription = None

    def setTopicDescription(self, topicDescription):
        """
        :param topicDescription: (Optional) 描述, 0-50个字符
        """
        self.topicDescription = topicDescription

