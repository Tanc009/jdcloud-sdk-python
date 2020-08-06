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


class EsLogFile(object):

    def __init__(self, key=None, fileName=None, updateTime=None, size=None):
        """
        :param key: (Optional) 日志唯一key值
        :param fileName: (Optional) 日志文件名称
        :param updateTime: (Optional) 日志更新时间
        :param size: (Optional) 文件大小
        """

        self.key = key
        self.fileName = fileName
        self.updateTime = updateTime
        self.size = size
