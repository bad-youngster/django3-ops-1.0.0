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
            return result
        except Exception as error:
            UtilClient.assert_as_string(error)

    def aliyun_get_single_ecs(self):
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id='cn-shanghai', instance_ids='["i-uf68ktdumlt44ouwk6d5"]')
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().describe_instances_with_options(
                describe_instances_request, runtime)
            return result
        except Exception as error:
            return (error)

    def aliyun_create_single_ecs(self):
        data_disk_0 = ecs_20140526_models.RunInstancesRequestDataDisk(
            snapshot_id='s-uf6i6pgbxx52mdnsk3r1')
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd', size='40', performance_level='PL0')
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-shanghai',
            system_disk=system_disk,
            instance_name='ttttttttttest',
            instance_type='ecs.c6.2xlarge',
            data_disk=list(data_disk_0),
            instance_charge_type='PostPaid',
            key_pair_name='jumpserver-key',
            security_group_id='sg-uf6f5uy0t9viaxdnch9o',
            v_switch_id='vsw-uf66g5mplx73r778vc5x1',
            image_id='m-uf65vulua3dv77lbafz6')
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().run_instances_with_options(
                run_instances_request, runtime)
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)
