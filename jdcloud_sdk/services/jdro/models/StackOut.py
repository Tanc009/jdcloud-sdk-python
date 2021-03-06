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


class StackOut(object):

    def __init__(self, action=None, canUpdate=None, createTime=None, disableRollback=None, id=None, input=None, name=None, output=None, region=None, stackVersion=None, status=None, statusReason=None, templateId=None, timeout=None, updateTime=None):
        """
        :param action: (Optional) 资源栈运行操作
        :param canUpdate: (Optional) 资源栈能否更新
        :param createTime: (Optional) 资源栈创建时间
        :param disableRollback: (Optional) 资源栈是否回滚设置
        :param id: (Optional) 资源栈ID
        :param input: (Optional) 资源栈输入信息，JSON格式，此字段只在查询资源栈详情describeStack时有值
        :param name: (Optional) 资源栈名称
        :param output: (Optional) 资源栈输出信息，JSON格式, 此字段只在查询资源栈详情describeStack时有值
        :param region: (Optional) 资源栈所在区域
        :param stackVersion: (Optional) 资源栈版本
        :param status: (Optional) 资源栈运行状态
        :param statusReason: (Optional) 资源栈运行状态原因
        :param templateId: (Optional) 资源栈使用的template ID
        :param timeout: (Optional) 资源栈超时时间
        :param updateTime: (Optional) 资源栈更新时间
        """

        self.action = action
        self.canUpdate = canUpdate
        self.createTime = createTime
        self.disableRollback = disableRollback
        self.id = id
        self.input = input
        self.name = name
        self.output = output
        self.region = region
        self.stackVersion = stackVersion
        self.status = status
        self.statusReason = statusReason
        self.templateId = templateId
        self.timeout = timeout
        self.updateTime = updateTime
