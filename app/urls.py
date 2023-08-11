# -*- coding: utf-8 -*-
# @Time  : 2023/08/07 13:30:39
# @Author: wy
from django.urls import path
from .views import nexus_infofile, mysql_install, user_add, user_get

urlpatterns = [
    path('nexusInfofile/', nexus_infofile, name='nexusInfofile'),
    path('mysqlInstall/', mysql_install, name='mysqlInstall'),
    path('userAdd/', user_add, name='useradd'),
    path('userGet/', user_get, name='userGet')
]
