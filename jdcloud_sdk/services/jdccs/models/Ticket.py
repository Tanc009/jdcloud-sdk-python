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


class Ticket(object):

    def __init__(self, ticketNo=None, ticketTemplateName=None, ticketTemplateCode=None, ticketTypeName=None, status=None, description=None, createdTime=None, closedTime=None, phone=None, email=None, idc=None, idcName=None):
        """
        :param ticketNo: (Optional) 工单编号
        :param ticketTemplateName: (Optional) 工单名称
        :param ticketTemplateCode: (Optional) 工单模板CODE
        :param ticketTypeName: (Optional) 工单类型
        :param status: (Optional) 工单状态 pendingReview:待审核 已撤销 revoked:已撤销 processing:处理中 pendingVerification:待核验 pendingClose:待关单 rejected:已拒绝 completed:已完成 cancelled:已取消 draft:草稿中
        :param description: (Optional) 描述
        :param createdTime: (Optional) 创建时间，遵循ISO8601标准，使用UTC时间，格式为：yyyy-MM-ddTHH:mm:ssZ
        :param closedTime: (Optional) 关闭时间，遵循ISO8601标准，使用UTC时间，格式为：yyyy-MM-ddTHH:mm:ssZ
        :param phone: (Optional) 电话
        :param email: (Optional) 邮箱
        :param idc: (Optional) 机房英文标识
        :param idcName: (Optional) 机房名称
        """

        self.ticketNo = ticketNo
        self.ticketTemplateName = ticketTemplateName
        self.ticketTemplateCode = ticketTemplateCode
        self.ticketTypeName = ticketTypeName
        self.status = status
        self.description = description
        self.createdTime = createdTime
        self.closedTime = closedTime
        self.phone = phone
        self.email = email
        self.idc = idc
        self.idcName = idcName
