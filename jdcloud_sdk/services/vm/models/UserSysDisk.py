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


class UserSysDisk(object):

    def __init__(self, pin=None, region=None, systemType=None, systemDiskSize=None):
        """
        :param pin: (Optional) 用户pin
        :param region: (Optional) 地域
        :param systemType: (Optional) 系统类型
        :param systemDiskSize: (Optional) 默认本地盘系统盘大小
        """

        self.pin = pin
        self.region = region
        self.systemType = systemType
        self.systemDiskSize = systemDiskSize
