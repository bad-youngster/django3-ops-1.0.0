# -*- coding: utf-8 -*-
# @Time  : 2023/08/29 15:12:02
# @Author: wy
import base64


def uncode(encode_str):
    decode_bytes = base64.b64decode(encode_str)
    decode_str = decode_bytes.decode('utf-8')
    return decode_str
