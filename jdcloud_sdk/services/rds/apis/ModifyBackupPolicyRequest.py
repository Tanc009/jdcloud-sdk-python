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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ModifyBackupPolicyRequest(JDCloudRequest):
    """
    修改RDS实例备份策略，目前仅支持用户修改“自动备份开始时间窗口”这个参数，其他参数暂不开放修改
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ModifyBackupPolicyRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:modifyBackupPolicy', 'POST', header, version)
        self.parameters = parameters


class ModifyBackupPolicyParameters(object):

    def __init__(self, regionId, instanceId, ):
        """
        :param regionId: 地域代码，取值范围参见[《各地域及可用区对照表》](../Enum-Definitions/Regions-AZ.md)
        :param instanceId: RDS 实例ID，唯一标识一个RDS实例
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.startWindow = None
        self.binlogRetentionPeriod = None
        self.binlogUsageLimit = None
        self.retentionPeriod = None
        self.cycleMode = None

    def setStartWindow(self, startWindow):
        """
        :param startWindow: (Optional) 自动备份开始时间窗口,例如：00:00-01:00，表示0点到1点开始进行数据库自动备份，备份完成时间则跟实例大小有关，不一定在这个时间范围中<br>SQL Server:范围00:00-23:59，时间范围差不得小于30分钟。<br>MySQL,只能是以下取值:<br>00:00-01:00<br>01:00-02:00<br>......<br>23:00-24:00
        """
        self.startWindow = startWindow

    def setBinlogRetentionPeriod(self, binlogRetentionPeriod):
        """
        :param binlogRetentionPeriod: (Optional) binlog本地保留周期，单位小时,范围1-168
        """
        self.binlogRetentionPeriod = binlogRetentionPeriod

    def setBinlogUsageLimit(self, binlogUsageLimit):
        """
        :param binlogUsageLimit: (Optional) binlog本地占用空间上限，单位%，范围1-50
        """
        self.binlogUsageLimit = binlogUsageLimit

    def setRetentionPeriod(self, retentionPeriod):
        """
        :param retentionPeriod: (Optional) 自动备份保留周期，单位天，范围7-730<br>当enhancedBackup为true时可修改<br>- 仅支持SQL Server
        """
        self.retentionPeriod = retentionPeriod

    def setCycleMode(self, cycleMode):
        """
        :param cycleMode: (Optional) 自动备份循环模式<br>1：表示每天都是全量备份<br>2：表示自动备份按照全量、增量、增量这样的方式进行，例如第1天是全量备份，第2、3天是增量备份；第4天又是全量备份，以此类推<br>当enhancedBackup为true时可修改<br>- 仅支持SQL Server
        """
        self.cycleMode = cycleMode

