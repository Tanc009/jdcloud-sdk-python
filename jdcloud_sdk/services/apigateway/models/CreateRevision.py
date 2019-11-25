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


class CreateRevision(object):

    def __init__(self, revision=None, baseRevision=None, revisionNote=None):
        """
        :param revision: (Optional) 修订版本号，如果创建版本时传回修订版本，此为必填项
        :param baseRevision: (Optional) 基于此版本，如果创建版本时传回修订版本，此为必填项
        :param revisionNote: (Optional) 修订备注
        """

        self.revision = revision
        self.baseRevision = baseRevision
        self.revisionNote = revisionNote
