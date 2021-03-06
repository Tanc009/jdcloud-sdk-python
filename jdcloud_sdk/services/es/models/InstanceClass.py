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


class InstanceClass(object):

    def __init__(self, nodeClass=None, nodeCpu=None, nodeMemoryGB=None, nodeDiskGB=None, nodeDiskType=None, nodeCount=None, masterClass=None, masterCpu=None, masterMemoryGB=None, masterDiskGB=None, masterDiskType=None, masterCount=None, coordinatingClass=None, coordinatingCpu=None, coordinatingMemoryGB=None, coordinatingDiskGB=None, coordinatingDiskType=None, coordinatingCount=None):
        """
        :param nodeClass: (Optional) data节点规格代码，规格代码对照关系参见：https://docs.jdcloud.com/cn/jcs-for-elasticsearch/specifications
        :param nodeCpu: (Optional) data节点cpu核数
        :param nodeMemoryGB: (Optional) data节点内存单位GB
        :param nodeDiskGB: (Optional) data节点存储大小单位GB
        :param nodeDiskType: (Optional) data节点存储类型
        :param nodeCount: (Optional) data节点数量
        :param masterClass: (Optional) master节点规格代码，规格代码对照关系参见：https://docs.jdcloud.com/cn/jcs-for-elasticsearch/specifications
        :param masterCpu: (Optional) master节点cpu核数
        :param masterMemoryGB: (Optional) master节点内存单位GB
        :param masterDiskGB: (Optional) master节点存储大小单位GB
        :param masterDiskType: (Optional) master节点存储类型
        :param masterCount: (Optional) master节点数量
        :param coordinatingClass: (Optional) coordinating节点规格代码，规格代码对照关系参见：https://docs.jdcloud.com/cn/jcs-for-elasticsearch/specifications
        :param coordinatingCpu: (Optional) coordinating节点cpu核数
        :param coordinatingMemoryGB: (Optional) coordinating节点内存单位GB
        :param coordinatingDiskGB: (Optional) coordinating节点存储大小单位GB
        :param coordinatingDiskType: (Optional) coordinating节点存储类型
        :param coordinatingCount: (Optional) coordinating节点数量
        """

        self.nodeClass = nodeClass
        self.nodeCpu = nodeCpu
        self.nodeMemoryGB = nodeMemoryGB
        self.nodeDiskGB = nodeDiskGB
        self.nodeDiskType = nodeDiskType
        self.nodeCount = nodeCount
        self.masterClass = masterClass
        self.masterCpu = masterCpu
        self.masterMemoryGB = masterMemoryGB
        self.masterDiskGB = masterDiskGB
        self.masterDiskType = masterDiskType
        self.masterCount = masterCount
        self.coordinatingClass = coordinatingClass
        self.coordinatingCpu = coordinatingCpu
        self.coordinatingMemoryGB = coordinatingMemoryGB
        self.coordinatingDiskGB = coordinatingDiskGB
        self.coordinatingDiskType = coordinatingDiskType
        self.coordinatingCount = coordinatingCount
