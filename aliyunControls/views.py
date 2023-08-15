# -*- coding: utf-8 -*-
# @Time  : 2023/08/15 16:20:13
# @Author: wy

from utilitys.aliyunapi import aliyun
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class aliyunEcs:

    def __init__(self) -> None:
        pass

    def aliyun_create_image(self):
        disk_device_mapping_0 = ecs_20140526_models.CreateImageRequestDiskDeviceMapping(
            snapshot_id='s-uf6a7f3ghd4xpqqc5p8m')
        create_image_request = ecs_20140526_models.CreateImageRequest(
            region_id='cn-shanghai',
            disk_device_mapping=[disk_device_mapping_0],
            image_name='snapimages')
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().create_image_with_options(
                create_image_request, runtime)
            print(result)
        except Exception as error:
            UtilClient.assert_as_string(error)