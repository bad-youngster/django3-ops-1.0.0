# -*- coding: utf-8 -*-
# @Time  : 2023/08/04 17:59:43
# @Author: wy
from utilitys.httpapi import nexus_api

class NexusStore:

    def nexus_upload(self):
        uri = 'v1/components/'
        query_params = {'repository': 'Mysql'}
        headers = {"Content-Type": "application/json"}
        result_data, result_code = nexus_api(method='GET',
                                             uri=uri,
                                             query_params=query_params,
                                             headers=headers)
        if result_code == 200:
            return result_data
        else:
            return result_code, result_data

    def nexus_download(self):
        pass