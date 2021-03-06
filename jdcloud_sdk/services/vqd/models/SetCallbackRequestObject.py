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


class SetCallbackRequestObject(object):

    def __init__(self, callbackType, callbackEvents, httpUrl=None):
        """
        :param callbackType:  回调方式，目前只支持 http
        :param httpUrl: (Optional) HTTP方式的该字段为必选项
        :param callbackEvents:  回调事件列表。
- VqdSuccess 视频质检成功
- VqdFailure 视频质检失败
- VqdStart 视频质检开始

        """

        self.callbackType = callbackType
        self.httpUrl = httpUrl
        self.callbackEvents = callbackEvents
