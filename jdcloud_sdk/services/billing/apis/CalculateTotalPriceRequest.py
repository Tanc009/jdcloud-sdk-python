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


class CalculateTotalPriceRequest(JDCloudRequest):
    """
    查询计费价格信息
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CalculateTotalPriceRequest, self).__init__(
            '/regions/{regionId}/calculateTotalPrice', 'POST', header, version)
        self.parameters = parameters


class CalculateTotalPriceParameters(object):

    def __init__(self, regionId, cmd, packageCount, ):
        """
        :param regionId: 
        :param cmd: 操作类型 1:创建 2:续费 3:升配 4:删除
        :param packageCount: 批量购买时数量
        """

        self.regionId = regionId
        self.cmd = cmd
        self.orderList = None
        self.operateTime = None
        self.promotionInfo = None
        self.clientType = None
        self.packageCount = packageCount
        self.processType = None

    def setOrderList(self, orderList):
        """
        :param orderList: (Optional) 计算价格的订单
        """
        self.orderList = orderList

    def setOperateTime(self, operateTime):
        """
        :param operateTime: (Optional) 操作时间，遵循ISO8601标准，使用UTC时间，格式为：YYYY-MM-DDTHH:mm:ssZ
        """
        self.operateTime = operateTime

    def setPromotionInfo(self, promotionInfo):
        """
        :param promotionInfo: (Optional) 1:折扣（不需要传） 2:免费活动3:付费活动 4:推荐码 5:会员价 [{"promotionType":1,"activityCode":123},{"promotionType":2,"activityCode":}]
        """
        self.promotionInfo = promotionInfo

    def setClientType(self, clientType):
        """
        :param clientType: (Optional) 客户端：1.PC端；2.移动端；
        """
        self.clientType = clientType

    def setProcessType(self, processType):
        """
        :param processType: (Optional) 临时升配时必传，3-临时升配
        """
        self.processType = processType

