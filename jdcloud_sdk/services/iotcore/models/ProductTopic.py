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


class ProductTopic(object):

    def __init__(self, topicId=None, topicShortName=None, topicOperation=None, topicDescription=None, createdTime=None, udpatedTime=None):
        """
        :param topicId: (Optional) 自定义topic唯一标识
        :param topicShortName: (Optional) Topic名称为必填，同一个产品下的Topic名称不能重复
只能包含字母，数字和下划线，最多64个字符，每个层级都不能为空
不能以/结尾

        :param topicOperation: (Optional) 操作权限，设备对该Topic类的操作权限，取值
pub:发布
sub:订阅

        :param topicDescription: (Optional) 描述, 0-50个字符
        :param createdTime: (Optional) 创建时间，创建时间，时间为东八区（UTC/GMT+08:00）
        :param udpatedTime: (Optional) 修改时间，创建时间，时间为东八区（UTC/GMT+08:00）
        """

        self.topicId = topicId
        self.topicShortName = topicShortName
        self.topicOperation = topicOperation
        self.topicDescription = topicDescription
        self.createdTime = createdTime
        self.udpatedTime = udpatedTime
