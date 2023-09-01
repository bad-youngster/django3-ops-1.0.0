# -*- coding: utf-8 -*-
# @Time  : 2023/08/15 16:20:13
# @Author: wy

from time import sleep
from utilitys.aliyunapi import aliyun
from alibabacloud_ecs20140526 import models as ecs_20140526_models
from alibabacloud_vpc20160428 import models as vpc_20160428_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_console.client import Client as ConsoleClient
from utilitys.utctime import utf_time, now_time
from utilitys.base64code import uncode
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
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def aliyun_get_vpc_attribute(self, args_dict):
        describe_vpc_attribute_request = vpc_20160428_models.DescribeVpcAttributeRequest(
            region_id='cn-shanghai', vpc_id=args_dict['VpcId'])
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_vpc_api(
            ).describe_vpc_attribute_with_options(
                describe_vpc_attribute_request, runtime)
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def aliyun_get_security_groups(self, args_dict):
        describe_security_groups_request = ecs_20140526_models.DescribeSecurityGroupsRequest(
            region_id='cn-shanghai', vpc_id=args_dict['VpcId'])
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api(
            ).describe_security_groups_with_options(
                describe_security_groups_request, runtime)
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def aliyun_create_single_ecs(self, args_dict):
        data_disk_0 = ecs_20140526_models.RunInstancesRequestDataDisk(
            snapshot_id=args_dict['data_snapid'])
        system_disk = ecs_20140526_models.RunInstancesRequestSystemDisk(
            category='cloud_essd', size='40', performance_level='PL0')
        run_instances_request = ecs_20140526_models.RunInstancesRequest(
            region_id=args_dict['regionId'],
            system_disk=system_disk,
            instance_name=args_dict['instanceName'],
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
        print(run_instances_request)
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().run_instances_with_options(
                run_instances_request, runtime)
            return result
        except Exception as error:
            print(error)

    def await_instance_status_to_running(self, instance_id):
        flag = True
        describe_instance_status_request = ecs_20140526_models.DescribeInstanceStatusRequest(
            region_id='cn-shanghai', instance_id=instance_id)
        runtime = util_models.RuntimeOptions()
        while flag:
            flag = False
            instance_status_list = aliyun().aliyun_ecs_api(
            ).describe_instance_status_with_options(
                describe_instance_status_request, runtime)
            for instance_status in instance_status_list.body.instance_statuses.instance_status:
                ConsoleClient.log(f'实例状态：{instance_status.status}')
                if instance_status.status != 'Running':
                    sleep(200)
                    flag = True
        return flag

        # return

    def describe_instance_status(self):
        """
        查询实例状态
        """
        region_id = 'cn-shanghai'
        instance_ids = ['i-uf670zp0t9e6x1ai2j8i']

        request = ecs_20140526_models.DescribeInstanceStatusRequest(
            region_id=region_id, instance_id=instance_ids)
        ConsoleClient.log(f'实例: {instance_ids}, 查询状态开始。')
        runtime = util_models.RuntimeOptions()
        try:
            responces = aliyun().aliyun_ecs_api(
            ).describe_instance_status_with_options(request, runtime)
            instance_status_list = responces.body.instance_statuses.instance_status
            ConsoleClient.log(
                f'实例: {instance_ids}, 查询状态成功。状态为: {UtilClient.to_jsonstring(instance_status_list)}'
            )
            return UtilClient.to_jsonstring(instance_status_list)
        except Exception as error:
            return error

    def aliyun_invoke_command(self, command_id):
        invoke_command_request = ecs_20140526_models.InvokeCommandRequest(
            region_id='cn-shanghai',
            command_id=command_id,
            instance_id=['i-uf670zp0t9e6x1ai2j8i'])
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().invoke_command_with_options(
                invoke_command_request, runtime)
            return result.body.invoke_id
        except Exception as error:
            ConsoleClient.log(f'{error}')

    def aliyun_describe_invocation_results(self, invoke_id):
        invoke_id = invoke_id
        sleep(20)
        describe_invocation_results_request = ecs_20140526_models.DescribeInvocationResultsRequest(
            region_id='cn-shanghai', invoke_id=invoke_id)
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api(
            ).describe_invocation_results_with_options(
                describe_invocation_results_request, runtime)
            return UtilClient.to_jsonstring(
                result.body.invocation.invocation_results.invocation_result)
        except Exception as error:
            ConsoleClient.log(f'{error}')

    def aliyun_stop_instance(self, instance_id):
        stop_instance_request = ecs_20140526_models.StopInstanceRequest(
            instance_id=instance_id)
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().stop_instance_with_options(
                stop_instance_request, runtime)
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def aliyun_start_instance(self, instance_id):
        start_instance_request = ecs_20140526_models.StartInstanceRequest(
            instance_id=instance_id)
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().start_instance_with_options(
                start_instance_request, runtime)
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def aliyun_reboot_instances(self, instance_id):
        reboot_instances_request = ecs_20140526_models.RebootInstancesRequest(
            region_id='cn-shanghai', instance_id=instance_id)
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api().reboot_instances_with_options(
                reboot_instances_request, runtime)
            return result
        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def aliyun_modify_instance_vpc_attribute(self, instance_id, vpc_id,
                                             v_switch_id, security_group_id):
        modify_instance_vpc_attribute_request = ecs_20140526_models.ModifyInstanceVpcAttributeRequest(
            instance_id=instance_id,
            vpc_id=vpc_id,
            v_switch_id=v_switch_id,
            security_group_id=security_group_id)
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_ecs_api(
            ).modify_instance_vpc_attribute_with_options(
                modify_instance_vpc_attribute_request, runtime)
            return result

        except Exception as error:
            UtilClient.assert_as_string(error.message)

    def main(self):
        aliyunEcs().await_instance_status_to_running(
            instance_id=['i-uf670zp0t9e6x1ai2j8i'])
        invoke_id = aliyunEcs().aliyun_invoke_command(
            command_id='c-sh03usaqvr6gg74')
        aliyunEcs().aliyun_describe_invocation_results(invoke_id=invoke_id)
        aliyunEcs().aliyun_stop_instance(instance_id='i-uf670zp0t9e6x1ai2j8i')
        aliyunEcs().describe_instance_status()
        sleep(20)
        aliyunEcs().aliyun_modify_instance_vpc_attribute(
            instance_id='i-uf670zp0t9e6x1ai2j8i',
            vpc_id='vpc-uf6lumr9mgrgu5uhr14ca',
            v_switch_id='vsw-uf6vgn14dmiginzidlgt9',
            security_group_id=['sg-uf6af54caswr420c113r'])
        sleep(20)
        aliyunEcs().aliyun_start_instance(instance_id='i-uf670zp0t9e6x1ai2j8i')
        sleep(20)
        aliyunEcs().await_instance_status_to_running(
            instance_id=['i-uf670zp0t9e6x1ai2j8i'])
        aliyunEcs().aliyun_invoke_command(command_id='c-sh03usaqvr6gg74')
        aliyunEcs().aliyun_reboot_instances(
            instance_id='i-uf670zp0t9e6x1ai2j8i')
