# -*- coding: utf-8 -*-
# @Time  : 2023/08/07 13:30:39
# @Author: wy
from django.urls import path
from .views import nexus_infofile, mysql_install, user_add, user_get, nexus_mysql_script, mysql_to_slave, select_single_ecs, get_single_ecs

urlpatterns = [
    path('nexusInfofile/', nexus_infofile, name='nexusInfofile'),
    path('nexusMysqlScript/', nexus_mysql_script, name='nexusMysqlScript'),
    path('mysqlInstall/', mysql_install, name='mysqlInstall'),
    path('mysqlToSlave/', mysql_to_slave, name='mysqlToSlave'),
    path('getSingleEcs/', get_single_ecs, name='getSingleEcs'),
    path('selectSingleEcs/', select_single_ecs, name='selectSingleEcs'),
    path('userAdd/', user_add, name='useradd'),
    path('userGet/', user_get, name='userGet')
]
