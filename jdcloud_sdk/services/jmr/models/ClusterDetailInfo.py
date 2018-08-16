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


class ClusterDetailInfo(object):

    def __init__(self, materNum=None, masterCore=None, masterMemory=None, masterDiskType=None, masterDiskVolume=None, masterInstanceType=None, masterInstanceInfo=None, slaveNum=None, slaveCore=None, slaveMemory=None, slaveDiskType=None, slaveDiskVolume=None, slaveInstanceType=None, slaveInstanceInfo=None):
        """
        :param materNum: (Optional) Master节点数量
        :param masterCore: (Optional) Master节点CPU
        :param masterMemory: (Optional) Master节点内存（推荐至少8G内存，否则服务可能会部署失败）
        :param masterDiskType: (Optional) "Master节点云盘类型，可传类型为（以下以“/”分割各类型）"
"NBD/NBD_SATA"
"分别代表：性能型/容量型"

        :param masterDiskVolume: (Optional) Master节点云盘容量，必须是10的整数倍，且大于20小于3000
        :param masterInstanceType: (Optional) Master节点规格，比如：g.n1.xlarge，更多规格请参考[文档](https://www.jdcloud.com/help/detail/296/isCatalog/1)
        :param masterInstanceInfo: (Optional) master节点实例信息
        :param slaveNum: (Optional) Slave节点数量
        :param slaveCore: (Optional) Slave节点CPU
        :param slaveMemory: (Optional) Slave节点内存(推荐至少4G内存，否则服务可能会部署失败)
        :param slaveDiskType: (Optional) "Slave节点云盘类型，可传类型为（以下以“/”分割各类型）"
"NBD/NBD_SATA"
"分别代表：性能型/容量型"

        :param slaveDiskVolume: (Optional) Slave节点云盘容量，必须是10的整数倍，且大于20小于3000
        :param slaveInstanceType: (Optional) Slave节点规格，比如：g.n1.xlarge，更多规格请参考[文档](https://www.jdcloud.com/help/detail/296/isCatalog/1)
        :param slaveInstanceInfo: (Optional) Slave节点实例信息
        """

        self.materNum = materNum
        self.masterCore = masterCore
        self.masterMemory = masterMemory
        self.masterDiskType = masterDiskType
        self.masterDiskVolume = masterDiskVolume
        self.masterInstanceType = masterInstanceType
        self.masterInstanceInfo = masterInstanceInfo
        self.slaveNum = slaveNum
        self.slaveCore = slaveCore
        self.slaveMemory = slaveMemory
        self.slaveDiskType = slaveDiskType
        self.slaveDiskVolume = slaveDiskVolume
        self.slaveInstanceType = slaveInstanceType
        self.slaveInstanceInfo = slaveInstanceInfo
