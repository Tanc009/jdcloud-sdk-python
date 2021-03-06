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


class NoticeVo(object):

    def __init__(self, uuid=None, id=None, title=None, type=None, goTop=None, inlet=None, createTime=None, updateTime=None, createPin=None, yn=None, content=None, startTime=None, endTime=None, site=None, pageNum=None, pageSize=None, lang=None, langId=None, ts=None):
        """
        :param uuid: (Optional) uuid
        :param id: (Optional) 主键id
        :param title: (Optional) 标题
        :param type: (Optional) 公告类型; 1:产品公告; 2:域名公告; 3:活动公告; 4:其他公告
        :param goTop: (Optional) 置顶; 100:不置顶; 1;2;3;4;5:置顶位置(数字不能重复)
        :param inlet: (Optional) 位置; 0:不显示; 1:左边; 2:左中; 3:中; 4:右中; 5:右
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 修改时间
        :param createPin: (Optional) 创建人
        :param yn: (Optional) 是否失效; 0:生效; 1:失效
        :param content: (Optional) 公告内容
        :param startTime: (Optional) 发送开始时间
        :param endTime: (Optional) 发送结束时间
        :param site: (Optional) 位置; 1:置顶; 2:入口
        :param pageNum: (Optional) 页码数
        :param pageSize: (Optional) 页显示数量
        :param lang: (Optional) 语言
        :param langId: (Optional) 中英文关联id
        :param ts: (Optional) 查询时间
        """

        self.uuid = uuid
        self.id = id
        self.title = title
        self.type = type
        self.goTop = goTop
        self.inlet = inlet
        self.createTime = createTime
        self.updateTime = updateTime
        self.createPin = createPin
        self.yn = yn
        self.content = content
        self.startTime = startTime
        self.endTime = endTime
        self.site = site
        self.pageNum = pageNum
        self.pageSize = pageSize
        self.lang = lang
        self.langId = langId
        self.ts = ts
