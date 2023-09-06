from django.test import TestCase

from utilitys.aliyunapi import aliyun
from app.views import aliyunEcs
from aliyunControls.aliyunMysqlViews import aliyunEcs
from aliyunControls.aliyunRedisViews import aliyunRedis
# Create your tests here.


class aliyunTest(TestCase):

    def aliyun_client(self):
        aliyun().aliyun_ecs_api()

    def snap_single_ecs_Test(self):
        aliyunEcs().snap_single_ecs()

    def describe_instance_status_test(self):
        aliyunEcs().describe_instance_status()


class aliyunInvokeTest(TestCase):

    def aliyunInvokeTest(self):
        aliyunEcs().aliyun_invoke_command()

    def aliyunInvokeResult(self):
        aliyunEcs().aliyun_describe_invocation_results()

    def aliyunRebootinstance(self):
        instance_id = ['i-uf670zp0t9e6x1ai2j8i']
        aliyunEcs().aliyun_reboot_instances(instance_id=instance_id)

    def aliyunStopInstance(self):
        instance_id = ['i-uf670zp0t9e6x1ai2j8i']
        aliyunEcs().await_instance_status_to_stoping(instance_id=instance_id)

    def aliyunMain(self):
        aliyunEcs().main()


class aliyunRedisTest(TestCase):

    def aliyunDescribeInstanceAttribute(self):
        aliyunRedis().aliyun_describe_instance_attribute()
    
    def aliyunDescribeAvailableResource(self):
        aliyunRedis().aliyun_upgrade_describe_available_resource()
