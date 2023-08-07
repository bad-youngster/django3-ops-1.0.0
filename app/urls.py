# -*- coding: utf-8 -*-
# @Time  : 2023/08/07 13:30:39
# @Author: wy
from django.urls import path
from .views import nexus_downfile

urlpatterns = [path('nexusDownfile/', nexus_downfile, name='nexusDownfile')]
