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


class Batch(object):

    def __init__(self, productKey=None, batchId=None, beginedTime=None, endTime=None, total=None, successes=None, failures=None, batchState=None, createdTime=None):
        """
        :param productKey: (Optional) 产品Key
        :param batchId: (Optional) 批次/批次ID
        :param beginedTime: (Optional) 开始时间，时间为东八区（UTC/GMT+08:00）
        :param endTime: (Optional) 结束时间，时间为东八区（UTC/GMT+08:00）
        :param total: (Optional) 设备总数
        :param successes: (Optional) 升级成功
        :param failures: (Optional) 升级失败
        :param batchState: (Optional) 状态：
updating:进行中
stoped:已终止
updated:已完成

        :param createdTime: (Optional) 上传时间，时间为东八区（UTC/GMT+08:00）
        """

        self.productKey = productKey
        self.batchId = batchId
        self.beginedTime = beginedTime
        self.endTime = endTime
        self.total = total
        self.successes = successes
        self.failures = failures
        self.batchState = batchState
        self.createdTime = createdTime
