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


class UserBindedGroups(object):

    def __init__(self, apiGroupId=None, groupName=None, region=None, authtime=None, authUserType=None, accessKey=None, appId=None, environment=None, revision=None):
        """
        :param apiGroupId: (Optional) 分组ID
        :param groupName: (Optional) 分组名称
        :param region: (Optional) 区域
        :param authtime: (Optional) 授权时间
        :param authUserType: (Optional) 授权用户类型
        :param accessKey: (Optional) Access Key
        :param appId: (Optional) api调用者的appid
        :param environment: (Optional) api部署的环境
        :param revision: (Optional) api版本
        """

        self.apiGroupId = apiGroupId
        self.groupName = groupName
        self.region = region
        self.authtime = authtime
        self.authUserType = authUserType
        self.accessKey = accessKey
        self.appId = appId
        self.environment = environment
        self.revision = revision
