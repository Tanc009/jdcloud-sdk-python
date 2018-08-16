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

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class ClusterExpansionRequest(JDCloudRequest):
    """
    集群扩容
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ClusterExpansionRequest, self).__init__(
            '/regions/{regionId}/cluster:expansion', 'POST', header, version)
        self.parameters = parameters


class ClusterExpansionParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 地域ID
        """

        self.regionId = regionId
        self.clusterId = None
        self.expansionNum = None

    def setClusterId(self, clusterId):
        """
        :param clusterId: (Optional) 需要扩容的集群ID
        """
        self.clusterId = clusterId

    def setExpansionNum(self, expansionNum):
        """
        :param expansionNum: (Optional) 扩容的数量
        """
        self.expansionNum = expansionNum

