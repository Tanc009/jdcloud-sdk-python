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


class RolePolicy(object):

    def __init__(self, policyName=None, description=None, type=None, policyJrn=None):
        """
        :param policyName: (Optional) 权限名称
        :param description: (Optional) 描述
        :param type: (Optional) 权限类型
        :param policyJrn: (Optional) 权限资源描
        """

        self.policyName = policyName
        self.description = description
        self.type = type
        self.policyJrn = policyJrn
