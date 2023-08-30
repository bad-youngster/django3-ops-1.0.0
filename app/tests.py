from django.test import TestCase

from utilitys.aliyunapi import aliyun
from app.views import aliyunEcs
from aliyunControls.views import aliyunEcs
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