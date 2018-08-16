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


class HardwareInfo(object):

    def __init__(self, nodeName=None, nodeType=None, nodeStatus=None, innerIp=None, outerIp=None, firewall=None, nodeCoreNum=None, nodeMemoryNum=None, nodeSystemInfo=None, nodeDiskType=None, nodeDiskVolume=None, serverId=None, msg=None, instanceType=None, instanceInfo=None):
        """
        :param nodeName: (Optional) 节点名称
        :param nodeType: (Optional) 节点类型
        :param nodeStatus: (Optional) 节点状态
        :param innerIp: (Optional) 内网IP
        :param outerIp: (Optional) 外网IP
        :param firewall: (Optional) 防火墙
        :param nodeCoreNum: (Optional) 节点核心数
        :param nodeMemoryNum: (Optional) 节点内存数
        :param nodeSystemInfo: (Optional) 节点系统信息
        :param nodeDiskType: (Optional) 节点硬盘类型
        :param nodeDiskVolume: (Optional) 节点硬盘容量
        :param serverId: (Optional) 节点实例ID
        :param msg: (Optional) 消息
        :param instanceType: (Optional) 节点硬件配置
        :param instanceInfo: (Optional) 节点硬件类型
        """

        self.nodeName = nodeName
        self.nodeType = nodeType
        self.nodeStatus = nodeStatus
        self.innerIp = innerIp
        self.outerIp = outerIp
        self.firewall = firewall
        self.nodeCoreNum = nodeCoreNum
        self.nodeMemoryNum = nodeMemoryNum
        self.nodeSystemInfo = nodeSystemInfo
        self.nodeDiskType = nodeDiskType
        self.nodeDiskVolume = nodeDiskVolume
        self.serverId = serverId
        self.msg = msg
        self.instanceType = instanceType
        self.instanceInfo = instanceInfo
