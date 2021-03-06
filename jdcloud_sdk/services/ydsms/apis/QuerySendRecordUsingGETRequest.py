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


class QuerySendRecordUsingGETRequest(JDCloudRequest):
    """
    查询短信发送记录
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(QuerySendRecordUsingGETRequest, self).__init__(
            '/smsApps/{appId}:querySendRecord', 'GET', header, version)
        self.parameters = parameters


class QuerySendRecordUsingGETParameters(object):

    def __init__(self, appId, endTime, startTime):
        """
        :param appId: 应用id
        :param endTime: 结束时间,pattern ="yyyy-MM-dd HH:mm:ss",timezone="GMT+8"
        :param startTime: 开始时间,pattern ="yyyy-MM-dd HH:mm:ss",timezone="GMT+8"
        """

        self.appId = appId
        self.sendStatus = None
        self.sendNumber = None
        self.templateId = None
        self.sign_id = None
        self.pageNumber = None
        self.pageSize = None
        self.endTime = endTime
        self.startTime = startTime

    def setSendStatus(self, sendStatus):
        """
        :param sendStatus: (Optional) 发送状态，0 全部状态 1 发送成功 2 发送失败 3 已发送未回执， 默认为0
        """
        self.sendStatus = sendStatus

    def setSendNumber(self, sendNumber):
        """
        :param sendNumber: (Optional) 手机号码
        """
        self.sendNumber = sendNumber

    def setTemplateId(self, templateId):
        """
        :param templateId: (Optional) 模板id
        """
        self.templateId = templateId

    def setSign_id(self, sign_id):
        """
        :param sign_id: (Optional) 签名id
        """
        self.sign_id = sign_id

    def setPageNumber(self, pageNumber):
        """
        :param pageNumber: (Optional) 页码
        """
        self.pageNumber = pageNumber

    def setPageSize(self, pageSize):
        """
        :param pageSize: (Optional) 分页大小
        """
        self.pageSize = pageSize

