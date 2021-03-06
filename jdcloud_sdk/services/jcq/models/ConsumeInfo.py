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


class ConsumeInfo(object):

    def __init__(self, consumerGroupId=None, messageConsumeStatus=None, successTimes=None, failedTimes=None, consumerInfoDetailList=None):
        """
        :param consumerGroupId: (Optional) 消费组名称
        :param messageConsumeStatus: (Optional) 消费状态[SUCCESS,UNCONSUMED,FAILED_RETRY,ALL_FAILED,UNKNOWN]
        :param successTimes: (Optional) 消费成功次数
        :param failedTimes: (Optional) 消费失败次数
        :param consumerInfoDetailList: (Optional) 消费组下面消费者详情
        """

        self.consumerGroupId = consumerGroupId
        self.messageConsumeStatus = messageConsumeStatus
        self.successTimes = successTimes
        self.failedTimes = failedTimes
        self.consumerInfoDetailList = consumerInfoDetailList
