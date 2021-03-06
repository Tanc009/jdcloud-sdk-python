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


class ViJobSummary(object):

    def __init__(self, jobId=None, templateId=None, region=None, inputBucket=None, inputFileKey=None, outputBucket=None, outputFilePath=None, createTime=None, updateTime=None):
        """
        :param jobId: (Optional) 作业ID
        :param templateId: (Optional) 模板ID
        :param region: (Optional) 对象存储区域，输入和输入同区域
        :param inputBucket: (Optional) 输入空间
        :param inputFileKey: (Optional) 输入文件
        :param outputBucket: (Optional) 输入空间
        :param outputFilePath: (Optional) 输入路径
        :param createTime: (Optional) 创建时间
        :param updateTime: (Optional) 更新时间
        """

        self.jobId = jobId
        self.templateId = templateId
        self.region = region
        self.inputBucket = inputBucket
        self.inputFileKey = inputFileKey
        self.outputBucket = outputBucket
        self.outputFilePath = outputFilePath
        self.createTime = createTime
        self.updateTime = updateTime
