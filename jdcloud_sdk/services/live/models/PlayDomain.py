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


class PlayDomain(object):

    def __init__(self, playDomain=None, playDomainCname=None, domainStatus=None, createTime=None, updateTime=None, regionId=None):
        """
        :param playDomain: (Optional) 播放域名
        :param playDomainCname: (Optional) 播放域名(Cname)
        :param domainStatus: (Optional) 直播域名状态
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        :param regionId: (Optional) 地域编码
        """

        self.playDomain = playDomain
        self.playDomainCname = playDomainCname
        self.domainStatus = domainStatus
        self.createTime = createTime
        self.updateTime = updateTime
        self.regionId = regionId
