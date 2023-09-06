# -*- coding: utf-8 -*-
# @Time  : 2023/09/04 13:23:55
# @Author: wy
from utilitys.aliyunapi import aliyun
from alibabacloud_r_kvstore20150101 import models as r_kvstore_20150101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient


class aliyunRedis:

    def aliyun_modify_instance_spec(self):
        modify_instance_spec_request = r_kvstore_20150101_models.ModifyInstanceSpecRequest(
            region_id='cn-shanghai',
            instance_id='r-uf6qnnkviurc7g6w0x',
            instance_class='redis.logic.sharding.6g.2db.0rodb.4proxy.default',
            order_type='UPGRADE'
            )
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_redis_api(
            ).modify_instance_spec_with_options(modify_instance_spec_request,
                                                runtime)
            print(result)
        except Exception as error:
            return error

    def aliyun_upgrade_describe_available_resource(self):
        describe_available_resource_request = r_kvstore_20150101_models.DescribeAvailableResourceRequest(
            region_id='cn-shanghai',
            engine='Redis',
            order_type='UPGRADE',
            instance_id='r-uf6mppsriyoe93n329')
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_redis_api(
            ).describe_available_resource_with_options(
                describe_available_resource_request, runtime)
            for e in result.body.available_zones.available_zone[
                    0].supported_engines.supported_engine[
                        0].supported_edition_types.supported_edition_type:
                if e.edition_type == 'Community':
                    for s in e.supported_series_types.supported_series_type[
                            0].supported_engine_versions.supported_engine_version[
                                0].supported_architecture_types.supported_architecture_type[
                                    0].supported_shard_numbers.supported_shard_number:
                        if s.shard_number == '2':
                            return UtilClient.to_jsonstring(
                                s.supported_node_types.supported_node_type[0].
                                available_resources.available_resource)

        except Exception as error:
            return error

    def aliyun_downgrade_describe_available_resource(self):
        describe_available_resource_request = r_kvstore_20150101_models.DescribeAvailableResourceRequest(
            region_id='cn-shanghai',
            instance_scene='professional',
            engine='Redis',
            order_type='DOWNGRADE',
            instance_id='r-uf6mppsriyoe93n329')
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_redis_api(
            ).describe_available_resource_with_options(
                describe_available_resource_request, runtime)
            print(result)
        except Exception as error:
            return error

    def aliyun_describe_instance_attribute(self):
        describe_instance_attribute_request = r_kvstore_20150101_models.DescribeInstanceAttributeRequest(
            instance_id='r-uf6mppsriyoe93n329')
        runtime = util_models.RuntimeOptions()
        try:
            result = aliyun().aliyun_redis_api(
            ).describe_instance_attribute_with_options(
                describe_instance_attribute_request, runtime)
            for s in result.body.instances.dbinstance_attribute:
                print(s)
        except Exception as error:
            return error