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


class InstanceTypeInfo(object):

    def __init__(self, instanceType=None, cpu=None, memory=None, gpuAmount=None, gpuSpec=None, localStorageSize=None, localStorageType=None, localStorageAmount=None, nicLimit=None):
        """
        :param instanceType: (Optional) 类型
        :param cpu: (Optional) 处理器核数，单位为C
        :param memory: (Optional) 内存大小，单位为M
        :param gpuAmount: (Optional) GPU 数量
        :param gpuSpec: (Optional) GPU 类型
        :param localStorageSize: (Optional) 本地存储的单盘容量
        :param localStorageType: (Optional) 本地存储的类型
        :param localStorageAmount: (Optional) 本地存储的数量
        :param nicLimit: (Optional) 支持弹性网卡的数量
        """

        self.instanceType = instanceType
        self.cpu = cpu
        self.memory = memory
        self.gpuAmount = gpuAmount
        self.gpuSpec = gpuSpec
        self.localStorageSize = localStorageSize
        self.localStorageType = localStorageType
        self.localStorageAmount = localStorageAmount
        self.nicLimit = nicLimit
