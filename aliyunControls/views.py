# -*- coding: utf-8 -*-
# @Time  : 2023/08/15 16:20:13
# @Author: wy

from utilitys.aliyunapi import aliyun
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from utilitys.utctime import utf_time, now_time
from app.models import AliyunEcsAssets, AliyunDescribeRegions
from django.core.serializers import serialize
import json


class aliyunEcs:

    def __init__(self) -> None:
        pass

    def aliyun_ecs_assets(self):
        aliyunEcsAssets = AliyunEcsAssets.objects.all()
        serialize_aliyunEcsAssets = json.loads(
            serialize('json', aliyunEcsAssets))
        fields = []
        for s in serialize_aliyunEcsAssets:
            fields.append(s['fields'])
        return fields

    def aliyun_ecs_regions(self):
        aliyunDescribeRegions = AliyunDescribeRegions.objects.all()
        serialize_aliyunDescribeRegions = json.loads(
            serialize('json', aliyunDescribeRegions))
        fields = []
        for s in serialize_aliyunDescribeRegions:
            fields.append(s['fields'])
        return fields

    def aliyun_region_instance_ecs(self, regionId):
        regionInstanceEcs = AliyunEcsAssets.objects.all().filter(
            regionId=regionId)
        serialize_regionInstanceEcs = json.loads(
            serialize('json', regionInstanceEcs))
        fields = []
        for s in serialize_regionInstanceEcs:
            fields.append(s['fields'])
        return fields

    def aliyun_create_image(self, args_dict):
        for a in args_dict:
            if a.get('SourceDiskType') == 'system':
                disk_device_mapping_0 = ecs_20140526_models.CreateImageRequestDiskDeviceMapping(
                    snapshot_id=a.get('SnapshotId'))
                create_image_request = ecs_20140526_models.CreateImageRequest(
                    region_id='cn-shanghai',
                    disk_device_mapping=[disk_device_mapping_0],
                    image_name='snapimages2')
                runtime = util_models.RuntimeOptions()
                try:
                    result = aliyun().aliyun_ecs_api(
                    ).create_image_with_options(create_image_request, runtime)
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

    def aliyun_select_single_ecs(self, args_dict):
        instanceIds = []
        instanceIds.append(args_dict['instanceId'])
        describe_instances_request = ecs_20140526_models.DescribeInstancesRequest(
            region_id=args_dict['regionId'], instance_ids=str(instanceIds))
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().describe_instances_with_options(
                describe_instances_request, runtime)
            return result
        except Exception as error:
            return error

    def select_snapshots_single_ecs(slef, args_dict):
        describe_snapshots_request = ecs_20140526_models.DescribeSnapshotsRequest(
            region_id=args_dict['regionId'],
            instance_id=args_dict['instanceId'])
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().describe_snapshots_with_options(
                describe_snapshots_request, runtime)
            snapshots = result.body.snapshots.snapshot
            snapshotss = []
            for s in snapshots:
                snaps = {}
                snaps['Progress'] = s.progress
                snaps['SnapshotId'] = s.snapshot_id
                snaps['SourceStorageType'] = s.source_storage_type
                snaps['SourceDiskSize'] = s.source_disk_size
                snaps['SourceDiskType'] = s.source_disk_type
                snaps['CreationTime'] = utf_time(s.creation_time)
                snaps['tags'] = s.tags.tag
                snapshotss.append(snaps)
            snapDisks = []
            for sn in snapshotss:
                if now_time() == sn.get('CreationTime'):
                    snapDisks.append(sn)
            return snapDisks
        except Exception as error:
            return error

    def aliyun_get_vpc(self):
        describe_vpcs_request = vpc_20160428_models.DescribeVpcsRequest(
            region_id='cn-shanghai')
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_vpc_api().describe_vpcs_with_options(
                describe_vpcs_request, runtime)
            for s in result.body.vpcs.vpc:
                print(s)
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def aliyun_create_single_ecs(self, args_dict):
        data_disk_0 = ecs_20140526_models.RunInstancesRequestDataDisk(
            snapshot_id=args_dict['data_snapid'])
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd', size='40', performance_level='PL0')
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id='cn-shanghai',
            system_disk=system_disk,
            instance_name='ttttttttttest',
            instance_type=args_dict['InstanceType'],
            data_disk=[data_disk_0],
            key_pair_name=args_dict['KeyPairName'],
            security_group_ids=args_dict['SecurityGroupIds'],
            v_switch_id=args_dict['VSwitchId'],
            image_id=args_dict['imageId'],
            period=1,
            period_unit='Month',
            auto_renew=False,
        )
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().run_instances_with_options(
                run_instances_request, runtime)
            return result
        except Exception as error:
            print(error)
