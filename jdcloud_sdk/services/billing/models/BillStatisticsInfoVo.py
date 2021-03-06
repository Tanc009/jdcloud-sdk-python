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


class BillStatisticsInfoVo(object):

    def __init__(self, totalFee=None, cashPayFee=None, cashCouponPayFee=None, balancePayFee=None, arrearFee=None, billFee=None, discountFee=None):
        """
        :param totalFee: (Optional) 总金额
        :param cashPayFee: (Optional) 现金支付金额
        :param cashCouponPayFee: (Optional) 优惠券支付金额
        :param balancePayFee: (Optional) 余额支付金额
        :param arrearFee: (Optional) 欠费金额
        :param billFee: (Optional) 账单金额
        :param discountFee: (Optional) 折扣金额
        """

        self.totalFee = totalFee
        self.cashPayFee = cashPayFee
        self.cashCouponPayFee = cashCouponPayFee
        self.balancePayFee = balancePayFee
        self.arrearFee = arrearFee
        self.billFee = billFee
        self.discountFee = discountFee
