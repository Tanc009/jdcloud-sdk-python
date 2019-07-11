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


class CreateWatermarkResultObject(object):

    def __init__(self, id=None, name=None, imgUrl=None, width=None, height=None, position=None, unit=None, offsetX=None, offsetY=None, createTime=None, updateTime=None):
        """
        :param id: (Optional) 水印ID
        :param name: (Optional) 水印名称
        :param imgUrl: (Optional) 图片地址
        :param width: (Optional) 宽度
        :param height: (Optional) 高度
        :param position: (Optional) 水印位置
        :param unit: (Optional) 偏移单位
        :param offsetX: (Optional) 水平偏移
        :param offsetY: (Optional) 竖直偏移
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        """

        self.id = id
        self.name = name
        self.imgUrl = imgUrl
        self.width = width
        self.height = height
        self.position = position
        self.unit = unit
        self.offsetX = offsetX
        self.offsetY = offsetY
        self.createTime = createTime
        self.updateTime = updateTime
