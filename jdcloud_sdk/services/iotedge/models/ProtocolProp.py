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


class ProtocolProp(object):

    def __init__(self, propName=None, propDesc=None, inputLength=None, inputDefault=None, unique=None, required=None):
        """
        :param propName: (Optional) 属性名称
        :param propDesc: (Optional) 属性描述
        :param inputLength: (Optional) 属性值长度限制
        :param inputDefault: (Optional) 属性默认值
        :param unique: (Optional) 是否必填,0-非唯一，1-唯一
        :param required: (Optional) 是否必填,0-非必填，1-必填
        """

        self.propName = propName
        self.propDesc = propDesc
        self.inputLength = inputLength
        self.inputDefault = inputDefault
        self.unique = unique
        self.required = required