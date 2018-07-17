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


class DetachDiskRequest(JDCloudRequest):
    """
    云主机缷载硬盘，主机和云盘没有未完成的任务时才可缷载
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(DetachDiskRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:detachDisk', 'POST', header, version)
        self.parameters = parameters


class DetachDiskParameters(object):

    def __init__(self, regionId, instanceId, diskId, ):
        """
        :param regionId: Region ID
        :param instanceId: Instance ID
        :param diskId: 云硬盘ID
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.diskId = diskId
        self.force = None

    def setForce(self, force):
        """
        :param force: (Optional) 强制缷载，默认False
        """
        self.force = force

