#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'zhanghr'
import sys


def getEnv():
    if len(sys.argv) > 1:
        env = sys.argv[1]
    else:
        env = 'test'
    config = {
        'test': {
            # 'baseurl': 'http://work.isyscore.net',
            'baseurl': 'http://10.30.30.66:8483',   # 运营后台host
            "loginName": "xxxxxx",  # 运营后台开发提供账号
            "password": "xxxxxx",  # 运营后台开发提供账号密码
            'projectId': 52,  # 自己的账号
        },
    }
    env_config = config['test']

    if env in config:
        env_config = config[env]
        # print(env_config)
    else:
        env_config = config['test']
        # print('不支持该环境:',env,'默认运行测试环境')
    return env_config


def switch():
    '''获取企业微信通知开关'''

    if len(sys.argv) > 2:
        weChatswitch = int(sys.argv[2])
        if weChatswitch == 1:
            print('111')
            return weChatswitch
        else:
            print('000')
            weChatswitch = 0
            return weChatswitch

    else:
        # 企业微信开关默认关
        weChatswitch = 0
        return weChatswitch


def getBuildNumber():
    '''获取jenkinsBuildNumber'''

    if len(sys.argv) > 3:
        jenkinsBuildNumber = int(sys.argv[3])
        print(jenkinsBuildNumber)
        return jenkinsBuildNumber

    else:
        # 获取jenkinsBuildNumber
        jenkinsBuildNumber = 87
        return jenkinsBuildNumber


env_config = getEnv()
