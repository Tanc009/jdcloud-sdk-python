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


class InstanceType(object):

    def __init__(self, family=None, instanceType=None, generation=None, cpu=None, memoryMB=None, nicLimit=None, desc=None, state=None, gpu=None, localDisks=None):
        """
        :param family: (Optional) 实例规格类型
        :param instanceType: (Optional) 实例规格，如g.n2.medium
        :param generation: (Optional) 实例规格代数
        :param cpu: (Optional) Cpu个数
        :param memoryMB: (Optional) 内存大小
        :param nicLimit: (Optional) 支持弹性网卡的数量
        :param desc: (Optional) 描述
        :param state: (Optional) 规格状态
        :param gpu: (Optional) Gpu配置
        :param localDisks: (Optional) 本地缓存盘配置
        """

        self.family = family
        self.instanceType = instanceType
        self.generation = generation
        self.cpu = cpu
        self.memoryMB = memoryMB
        self.nicLimit = nicLimit
        self.desc = desc
        self.state = state
        self.gpu = gpu
        self.localDisks = localDisks
