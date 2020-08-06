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


class ResizeInstanceRequest(JDCloudRequest):
    """
    云主机变更实例规格<br>
云主机的状态必须为<b>stopped</b>状态。<br>
以下情况的云主机，不允许在一代与二代实例规格间互相调整，例：不允许g.n1与g.n2之间互相调配<br>
1、16年创建的云硬盘做系统盘的云主机<br>
2、本地盘(local类型)做系统盘的云主机。<br>
3、使用高可用组(Ag)创建的云主机。<br>
如果当前主机中的弹性网卡数量，大于新实例规格允许的弹性网卡数量，会返回错误。可查询<a href="http://docs.jdcloud.com/virtual-machines/api/describeinstancetypes">DescribeInstanceTypes</a>接口获得指定地域及可用区下的实例规格信息。<br>
当前主机所使用的镜像，需要支持要变更的目标实例规格，否则返回错误。可查询<a href="http://docs.jdcloud.com/virtual-machines/api/describeimageconstraints">DescribeImageConstraints</a>接口获得指定镜像的实例规格限制信息。<br>
云主机欠费或到期时，无法更改实例规格。

    """

    def __init__(self, parameters, header=None, version="v1"):
        super(ResizeInstanceRequest, self).__init__(
            '/regions/{regionId}/instances/{instanceId}:resizeInstance', 'POST', header, version)
        self.parameters = parameters


class ResizeInstanceParameters(object):

    def __init__(self, regionId, instanceId, instanceType):
        """
        :param regionId: 地域ID
        :param instanceId: 云主机ID
        :param instanceType: 实例规格，可查询<a href="http://docs.jdcloud.com/virtual-machines/api/describeinstancetypes">DescribeInstanceTypes</a>接口获得指定地域或可用区的规格信息。
        """

        self.regionId = regionId
        self.instanceId = instanceId
        self.instanceType = instanceType

