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


class TOSAuthInfo(object):

    def __init__(self, accessKey=None, secretKey=None, authVersion=None, authHeaders=None, expireTime=None):
        """
        :param accessKey: (Optional) 密钥
        :param secretKey: (Optional) 密钥的加密密钥
        :param authVersion: (Optional) 版本[v1,v2]
        :param authHeaders: (Optional) 
        :param expireTime: (Optional) 单位s，默认 900
        """

        self.accessKey = accessKey
        self.secretKey = secretKey
        self.authVersion = authVersion
        self.authHeaders = authHeaders
        self.expireTime = expireTime
