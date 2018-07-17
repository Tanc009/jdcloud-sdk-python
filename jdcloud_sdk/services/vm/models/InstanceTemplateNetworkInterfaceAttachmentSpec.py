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


class InstanceTemplateNetworkInterfaceAttachmentSpec(object):

    def __init__(self, networkInterface, deviceIndex=None, autoDelete=None):
        """
        :param deviceIndex: (Optional) 设备Index；主网卡的index必须为1；当前仅支持主网卡
        :param autoDelete: (Optional) 指明删除实例时是否删除网卡，默认true；当前只能是true
        :param networkInterface:  网卡接口规范；此字段当前必填
        """

        self.deviceIndex = deviceIndex
        self.autoDelete = autoDelete
        self.networkInterface = networkInterface
