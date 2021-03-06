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


class TransReqVo(object):

    def __init__(self, sourceErp=None, targetErp=None, itemId=None, itemName=None, timestamp=None, signature=None):
        """
        :param sourceErp: (Optional) 离职人erp
        :param targetErp: (Optional) 接收人erp
        :param itemId: (Optional) 交接项id
        :param itemName: (Optional) 交接项名称，如果交接项ID为空则交接项名称必须确保唯⼀
        :param timestamp: (Optional) 时间戳，请求时间与系统时间不得超过10分钟，否则返回403
        :param signature: (Optional) 鉴权签名，md5加密（32位小写）
        """

        self.sourceErp = sourceErp
        self.targetErp = targetErp
        self.itemId = itemId
        self.itemName = itemName
        self.timestamp = timestamp
        self.signature = signature
