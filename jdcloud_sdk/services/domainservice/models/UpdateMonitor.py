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


class UpdateMonitor(object):

    def __init__(self, alarmLimit, id, ipBackup01, ipBackup02, monitorEnable, monitorFreq, monitorPort, monitorRule, monitorUri, notifyEmailEnable, notifyMsgBarEnable, protocol, stopRecoverRule, switchRecoverRule, backupAddressList=None, notifySmsEnable=None):
        """
        :param alarmLimit:  连续几次触发报警
        :param id:  监控项ID
        :param ipBackup01:  备用地址1
        :param ipBackup02:  备用地址2
        :param backupAddressList: (Optional) 备用地址列表，存在该参数时，可不填写参数备用地址1、备用地址2
        :param monitorEnable:  监控状况 开启监控:2，暂停监控:4
        :param monitorFreq:  监控频率，单位秒
        :param monitorPort:  监控端口
        :param monitorRule:  不做任何修改0，强制暂停解析记录1，自动切换到备用地址2
        :param monitorUri:  监控路径
        :param notifyEmailEnable:  不发送邮件:0， 发送邮件:1
        :param notifyMsgBarEnable:  不发送通知栏:0， 发送通知栏:1
        :param notifySmsEnable: (Optional) 不发送短信:0， 发送短信:1
        :param protocol:  https 0，https 1
        :param stopRecoverRule:  0自动恢复 1手动恢复
        :param switchRecoverRule:  0自动恢复至主host 1手动恢复至主host
        """

        self.alarmLimit = alarmLimit
        self.id = id
        self.ipBackup01 = ipBackup01
        self.ipBackup02 = ipBackup02
        self.backupAddressList = backupAddressList
        self.monitorEnable = monitorEnable
        self.monitorFreq = monitorFreq
        self.monitorPort = monitorPort
        self.monitorRule = monitorRule
        self.monitorUri = monitorUri
        self.notifyEmailEnable = notifyEmailEnable
        self.notifyMsgBarEnable = notifyMsgBarEnable
        self.notifySmsEnable = notifySmsEnable
        self.protocol = protocol
        self.stopRecoverRule = stopRecoverRule
        self.switchRecoverRule = switchRecoverRule