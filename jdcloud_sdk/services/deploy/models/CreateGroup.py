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


class CreateGroup(object):

    def __init__(self, groupName, appId, deployMethod, lbStatus, repeatPolicy, noticeTrigger, rollback, desc=None, instances=None, blueInstances=None, greenInstances=None, concurrencyUnit=None, concurrencyNum=None, concurrencyPct=None, lbInstance=None, lbBackend=None, noticeMethod=None, jdsfRegisterId=None):
        """
        :param groupName:  部署组名称
        :param appId:  应用ID
        :param desc: (Optional) 描述
        :param deployMethod:  部署方式：1滚动部署，2蓝绿部署
        :param instances: (Optional) 部署实例（滚动部署）
        :param blueInstances: (Optional) 部署实例（蓝绿部署蓝组）
        :param greenInstances: (Optional) 部署实例（蓝绿部署绿组）
        :param concurrencyUnit: (Optional) 并发单位
        :param concurrencyNum: (Optional) 并发机器数
        :param concurrencyPct: (Optional) 并发度
        :param lbStatus:  负载均衡：1启动，2禁用
        :param lbInstance: (Optional) lb实例
        :param lbBackend: (Optional) lb lb后端服务
        :param repeatPolicy:  同名文件处理方式：1部署失败，2覆盖，3保留
        :param noticeTrigger:  通知频率：0不发送，1消息，2邮件，3短信
        :param noticeMethod: (Optional) 通知方式：1消息，2邮件，3短信
        :param rollback:  自动回滚：1开启，2禁用
        :param jdsfRegisterId: (Optional) 分布式服务框架ID
        """

        self.groupName = groupName
        self.appId = appId
        self.desc = desc
        self.deployMethod = deployMethod
        self.instances = instances
        self.blueInstances = blueInstances
        self.greenInstances = greenInstances
        self.concurrencyUnit = concurrencyUnit
        self.concurrencyNum = concurrencyNum
        self.concurrencyPct = concurrencyPct
        self.lbStatus = lbStatus
        self.lbInstance = lbInstance
        self.lbBackend = lbBackend
        self.repeatPolicy = repeatPolicy
        self.noticeTrigger = noticeTrigger
        self.noticeMethod = noticeMethod
        self.rollback = rollback
        self.jdsfRegisterId = jdsfRegisterId
