from django.test import TestCase

from utilitys.aliyunapi import aliyun
from app.views import aliyunEcs

# Create your tests here.


class aliyunTest(TestCase):

    def aliyun_client(self):
        aliyun().aliyun_ecs_api()

    def snap_single_ecs_Test(self):
        aliyunEcs().snap_single_ecs()
    
    def describe_instance_status_test(self):
        aliyunEcs().describe_instance_status()
