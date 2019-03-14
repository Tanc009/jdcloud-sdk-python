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


class Action(object):

    def __init__(self, actionId=None, actionType=None, operationType=None, configuration=None):
        """
        :param actionId: (Optional) 
        :param actionType: (Optional) 动作类型，包括：handle（数据处理）、forward（转发数据）和failure（转发失败）
        :param operationType: (Optional) 操作类型,包括：JCQ、JsScript、Kafka、RabbitMq、RDS和ES
        :param configuration: (Optional) 规则动作的配置信息, Configuration是JSONObject格式，会根据不同的规则动作，形成不同的JSONObject格式，即不同的配置信息格式。
        """

        self.actionId = actionId
        self.actionType = actionType
        self.operationType = operationType
        self.configuration = configuration
