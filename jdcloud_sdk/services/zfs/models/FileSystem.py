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


class FileSystem(object):

    def __init__(self, fileSystemId=None, name=None, description=None, numberOfMountTargets=None, sizeByte=None, status=None, createTime=None, dnsName=None):
        """
        :param fileSystemId: (Optional) 文件系统ID
        :param name: (Optional) 文件系统名称(参数规则：不可为空，只支持中文、数字、大小写字母、英文下划线“_”及中划线“-”，且不能超过32字符)
        :param description: (Optional) 文件系统描述(参数规则：不能超过256字符)
        :param numberOfMountTargets: (Optional) 挂载目标个数
        :param sizeByte: (Optional) 最近一次统计的文件系统的使用量单位为:Byte
        :param status: (Optional) 文件系统状态(创建中:creating、可用:available、使用中:in-use、删除中:deleting)
        :param createTime: (Optional) 创建时间
        :param dnsName: (Optional) dns名称
        """

        self.fileSystemId = fileSystemId
        self.name = name
        self.description = description
        self.numberOfMountTargets = numberOfMountTargets
        self.sizeByte = sizeByte
        self.status = status
        self.createTime = createTime
        self.dnsName = dnsName