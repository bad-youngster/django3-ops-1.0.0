# -*- coding: utf-8 -*-
# @Time  : 2023/08/04 17:09:15
# @Author: wy
from django.conf import settings
import requests


def nexus_api(method, uri, query_params, headers):
    vm_url = settings.NEXUS_API + uri
    auth = (settings.NEXUS_USER, settings.NEXUS_PASS)
    try:
        response = requests.request(method,
                                    vm_url,
                                    params=query_params,
                                    headers=headers,
                                    auth=auth)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Decode the response content as JSON, if applicable
        try:
            response_data = response.json()
        except ValueError:
            response_data = response.text

        return response_data, response.status_code

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None, None