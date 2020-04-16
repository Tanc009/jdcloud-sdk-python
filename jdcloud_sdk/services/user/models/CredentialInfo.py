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


class CredentialInfo(object):

    def __init__(self, accessKey=None, secretKey=None, sessionToken=None, expiration=None, rolePin=None):
        """
        :param accessKey: (Optional) 临时身份凭证AK
        :param secretKey: (Optional) 临时身份凭证SK
        :param sessionToken: (Optional) 临时身份凭证令牌
        :param expiration: (Optional) token失效时点（sdk内对token有效期做了校验，接入方不需要关注该字段）
        :param rolePin: (Optional) 角色所属主账号，产品线判断灰度使用（非内测公测产品线不用关注该字段）
        """

        self.accessKey = accessKey
        self.secretKey = secretKey
        self.sessionToken = sessionToken
        self.expiration = expiration
        self.rolePin = rolePin
