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


class Snapshot(object):

    def __init__(self, snapshotId=None, type=None, createTime=None, indices=None, status=None):
        """
        :param snapshotId: (Optional) 快照ID
        :param type: (Optional) 快照类型，Auto：自动，Manual：人工
        :param createTime: (Optional) 创建时间，遵循ISO8601标准，使用UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ
        :param indices: (Optional) 备份的索引
        :param status: (Optional) 快照状态，Available：可用，Unavailable：不可用，Creating：创建中
        """

        self.snapshotId = snapshotId
        self.type = type
        self.createTime = createTime
        self.indices = indices
        self.status = status
