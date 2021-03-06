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


class SummaryBill(object):

    def __init__(self, balancePayFee=None, discountFee=None, realTotalFee=None, arrearFee=None, totalFee=None, cashPayFee=None, cashCouponFee=None, pin=None):
        """
        :param balancePayFee: (Optional) 余额支付金额
        :param discountFee: (Optional) 优惠金额
        :param realTotalFee: (Optional) 优惠后金额
        :param arrearFee: (Optional) 欠费金额
        :param totalFee: (Optional) 优惠前金额
        :param cashPayFee: (Optional) 现金支付金额
        :param cashCouponFee: (Optional) 代金券支付金额
        :param pin: (Optional) pin
        """

        self.balancePayFee = balancePayFee
        self.discountFee = discountFee
        self.realTotalFee = realTotalFee
        self.arrearFee = arrearFee
        self.totalFee = totalFee
        self.cashPayFee = cashPayFee
        self.cashCouponFee = cashCouponFee
        self.pin = pin
