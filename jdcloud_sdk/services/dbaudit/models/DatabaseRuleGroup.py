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


class DatabaseRuleGroup(object):

    def __init__(self, ruleGroupId=None, ruleGroupName=None, databaseRule=None):
        """
        :param ruleGroupId: (Optional) 规则组ID
        :param ruleGroupName: (Optional) 规则组名称
        :param databaseRule: (Optional) 规则组内的所有规则
        """

        self.ruleGroupId = ruleGroupId
        self.ruleGroupName = ruleGroupName
        self.databaseRule = databaseRule
