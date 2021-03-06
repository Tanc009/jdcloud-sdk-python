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


class SnapshotTemplateSpriteConfigInfo(object):

    def __init__(self, startTime=None, intervalTime=None, rows=None, columns=None, format=None, frameType=None, cellWidth=None, cellHeight=None, doKeepShots=None):
        """
        :param startTime: (Optional) 截图开始时间，单位毫秒，缺省值为 0
        :param intervalTime: (Optional) 截图间隔时间，单位毫秒，缺省值为 0
        :param rows: (Optional) 小图行数，取值必须大于 0
        :param columns: (Optional) 小图列数，取值必须大于 0
假设 rows * columns = N
若 intervalTime 为 0，则从 startTime 开始，平均截取 N 张图片；
若 intervalTime 不为 0，则从 startTime 开始，依次间隔截图，最多截取 N 张图，若实际截图张数小于 N，则雪碧图合成时用黑图填充

        :param format: (Optional) 截图存储格式。取值范围：png、jpg
        :param frameType: (Optional) 截图帧类型。取值范围：any、key
        :param cellWidth: (Optional) 截图宽度，单位 px，取值须大于 0
        :param cellHeight: (Optional) 截图高度，单位 px，取值须大于 0
若 width、height 都不为 0，则截图分辨率为 width * height
若 width、height 某一项为 0，则该项随另一项等比缩放
若 width、height 两项都为 0, 则截图分辨率随源视频

        :param doKeepShots: (Optional) 是否保留原截图
        """

        self.startTime = startTime
        self.intervalTime = intervalTime
        self.rows = rows
        self.columns = columns
        self.format = format
        self.frameType = frameType
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.doKeepShots = doKeepShots
