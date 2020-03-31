#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'zhanghr'

from common import env_config
import requests

loginName = env_config.env_config['loginName']
password = env_config.env_config['password']


def just_get_cookie():
    host = "http://10.30.30.66:8483"
    # 登录运营平台获取运营平台的cookie
    loginName = "xxxxxx"
    password = "xxxxxx"
    headers_yunying = {"content-type": 'application/x-www-form-urlencoded'}
    yunying_url = host +"/api/phoenix/cloud/authentication/login"
    yunying_data = {"loginName": loginName, "password": password}
    cookie = requests.post(url=yunying_url,
                               data=yunying_data,
                               headers=headers_yunying,
                               verify=False).headers['Set-Cookie']

    # print(Set_Cookie)
    return cookie

