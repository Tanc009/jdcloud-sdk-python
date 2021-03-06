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


class AgentInfo(object):

    def __init__(self, agnetId=None, hostId=None, osType=None, hostName=None, agentStatus=None, ifritStatus=None, auditCount=None, limitStatus=None, cpuLimit=None, memLimit=None, cpuPercent=None, memPercert=None, memTotal=None, cpuTotal=None, installTime=None, lastUpdateTime=None):
        """
        :param agnetId: (Optional) agentID
        :param hostId: (Optional) 主机ID
        :param osType: (Optional) 操作系统类型 Windows Server | CentOS
        :param hostName: (Optional) 主机名称
        :param agentStatus: (Optional) agent运行状态 0 安装中 1 运行中 2 离线 3 已卸载 4 待配置 5 安装失败(ifrit安装失败，需要重试或者手动安装)
        :param ifritStatus: (Optional) ifrit客户端的状态 0 安装成功 1 离线状态
        :param auditCount: (Optional) agent审计的数据库数量
        :param limitStatus: (Optional) 是否限制CPU/MEM
0 否 
1 是 此时cpuLimit/memLimit为必填项

        :param cpuLimit: (Optional) CPU限制，单位%
        :param memLimit: (Optional) 内存限制，单位%
        :param cpuPercent: (Optional) CPU实时占比，单位%
        :param memPercert: (Optional) 内存实时占比，单位%
        :param memTotal: (Optional) 内存总量,单位MB
        :param cpuTotal: (Optional) CPU核数,单位核数
        :param installTime: (Optional) agent安装时间
        :param lastUpdateTime: (Optional) 最后一次上报数据时间
        """

        self.agnetId = agnetId
        self.hostId = hostId
        self.osType = osType
        self.hostName = hostName
        self.agentStatus = agentStatus
        self.ifritStatus = ifritStatus
        self.auditCount = auditCount
        self.limitStatus = limitStatus
        self.cpuLimit = cpuLimit
        self.memLimit = memLimit
        self.cpuPercent = cpuPercent
        self.memPercert = memPercert
        self.memTotal = memTotal
        self.cpuTotal = cpuTotal
        self.installTime = installTime
        self.lastUpdateTime = lastUpdateTime
