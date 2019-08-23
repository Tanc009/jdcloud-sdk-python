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


class Backup(object):

    def __init__(self, baseId, backupFileName, cacheInstanceId, backupStartTime, backupEndTime, backupType, backupSize, backupStatus, backupDownloadURL, ):
        """
        :param baseId:  备份操作ID
        :param backupFileName:  备份文件的名称
        :param cacheInstanceId:  备份文件对应的实例ID
        :param backupStartTime:  备份开始时间（ISO 8601标准的UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ）
        :param backupEndTime:  备份结束时间（ISO 8601标准的UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ）
        :param backupType:  备份类型，1表示手动备份，0表示自动备份
        :param backupSize:  备份文件总字节大小，如果实例是集群版，则表示每个分片备份文件大小的总和
        :param backupStatus:  备份任务状态状态，0表示备份中，1表示失败，2表示成功
        :param backupDownloadURL:  备份文件下载地址（已废弃，调用获取备份文件下载地址接口获取）
        """

        self.baseId = baseId
        self.backupFileName = backupFileName
        self.cacheInstanceId = cacheInstanceId
        self.backupStartTime = backupStartTime
        self.backupEndTime = backupEndTime
        self.backupType = backupType
        self.backupSize = backupSize
        self.backupStatus = backupStatus
        self.backupDownloadURL = backupDownloadURL
