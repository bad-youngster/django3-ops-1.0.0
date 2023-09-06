# -*- coding: utf-8 -*-
# @Time  : 2023/08/15 16:21:07
# @Author: wy
from django.conf import settings

from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_vpc20160428.client import Client as Vpc20160428Client
from alibabacloud_r_kvstore20150101.client import Client as R_kvstore20150101Client
from alibabacloud_tea_openapi import models as open_api_models


class aliyun:

    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Ecs20140526Client:
        config = open_api_models.Config(access_key_id=access_key_id,
                                        access_key_secret=access_key_secret)
        config.endpoint = f'ecs.cn-shanghai.aliyuncs.com'
        return Ecs20140526Client(config)

    @staticmethod
    def create_vpc_client(access_key_id: str,
                          access_key_secret: str) -> Vpc20160428Client:
        config = open_api_models.Config(access_key_id=access_key_id,
                                        access_key_secret=access_key_secret)
        config.endpoint = f'vpc.cn-shanghai.aliyuncs.com'
        return Vpc20160428Client(config)

    @staticmethod
    def create_redis_client(access_key_id: str,
                            access_key_secret: str) -> R_kvstore20150101Client:
        config = open_api_models.Config(access_key_id=access_key_id,
                                        access_key_secret=access_key_secret)
        config.endpoint = f'r-kvstore.aliyuncs.com'
        return R_kvstore20150101Client(config)

    def aliyun_ecs_api(self):
        try:
            client = aliyun.create_client(settings.ALIYUN_ACCESS_KEY_ID,
                                          settings.ALIYUN_ACCESS_KEY_SECRET)
            return client
        except Exception as error:
            return error

    def aliyun_vpc_api(self):
        try:
            client = aliyun.create_vpc_client(
                settings.ALIYUN_ACCESS_KEY_ID,
                settings.ALIYUN_ACCESS_KEY_SECRET)
            return client
        except Exception as error:
            return error

    def aliyun_redis_api(self):
        try:
            client = aliyun.create_redis_client(
                settings.ALIYUN_ACCESS_KEY_ID,
                settings.ALIYUN_ACCESS_KEY_SECRET)
            return client
        except Exception as error:
            return error