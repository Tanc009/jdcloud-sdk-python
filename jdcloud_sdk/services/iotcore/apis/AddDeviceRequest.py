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


class AddDeviceRequest(JDCloudRequest):
    """
    注册单个设备并返回秘钥信息
    """

    def __init__(self, parameters, header=None, version="v2"):
        super(AddDeviceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}/device:add', 'POST', header, version)
        self.parameters = parameters


class AddDeviceParameters(object):

    def __init__(self, instanceId, regionId, ):
        """
        :param instanceId: 设备归属的实例ID
        :param regionId: 设备归属的实例所在区域
        """

        self.instanceId = instanceId
        self.regionId = regionId
        self.deviceName = None
        self.productKey = None
        self.model = None
        self.manufacturer = None
        self.description = None

    def setDeviceName(self, deviceName):
        """
        :param deviceName: (Optional) 设备名称
        """
        self.deviceName = deviceName

    def setProductKey(self, productKey):
        """
        :param productKey: (Optional) 设备所归属的产品
        """
        self.productKey = productKey

    def setModel(self, model):
        """
        :param model: (Optional) 设备型号
        """
        self.model = model

    def setManufacturer(self, manufacturer):
        """
        :param manufacturer: (Optional) 厂商
        """
        self.manufacturer = manufacturer

    def setDescription(self, description):
        """
        :param description: (Optional) 设备描述
        """
        self.description = description

