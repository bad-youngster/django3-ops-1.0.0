from django.test import TestCase

from utilitys.aliyunapi import aliyun

# Create your tests here.


class aliyunTest(TestCase):

    def aliyun_client(self):
        aliyun().aliyun_ecs_api()
