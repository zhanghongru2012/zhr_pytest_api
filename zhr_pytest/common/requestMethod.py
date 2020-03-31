#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'zhanghr'
import requests
import time
from common import getCookie
from common import env_config
import json

cookie = getCookie.just_get_cookie()


class RequestMethod:
    def __init__(self):

        """初始化参数"""
        self.baseurl = env_config.env_config['baseurl']
        # self.url_web = self.baseurl +env_config.env_config['url_web']
        self.base_header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
            "cookie": cookie
        }
        self.form_header = self.base_header.copy()
        self.form_header['Content-Type'] = 'multipart/form-data'
        self.json_header = self.base_header.copy()
        self.json_header['Content-Type'] = 'application/json'
        self.form_urlencoded_header = self.base_header.copy()
        self.form_urlencoded_header['Content-Type'] = 'application/x-www-form-urlencoded'

        self.timeout = 120

    def get(self, url, params):
        """定义普通get请求"""
        test_url = self.baseurl + url
        try:
             result = requests.get(url=test_url, params=params, headers=self.base_header, timeout=self.timeout)
             return result
        except Exception as e:
             return print('发生异常：%s' % e)

    def delete(self, url, params):
        """定义delete请求"""
        test_url = self.baseurl + url
        try:
            result = requests.delete(url=test_url, params=params, headers=self.base_header, timeout=self.timeout)
            return result
        except Exception as e:
            return print('发生异常：%s' % e)

    def post(self, url, params, data):
        """定义post请求"""
        test_url = self.baseurl + url
        try:
            return requests.post(url=test_url, params=params, data=data, headers=self.form_header, timeout=self.timeout)
        except Exception as e:
            return print('发生异常：%s' % e)

    def put(self, url, params, data):
        """定义put请求"""
        test_url = self.baseurl + url
        try:
            return requests.put(url=test_url, params=params, data=data, headers=self.form_header, timeout=self.timeout)
        except Exception as e:
            return print('发生异常：%s' % e)

    def post_json(self, url, params, data):
        """定义post请求"""
        test_url = self.baseurl + url
        try:
            return requests.post(url=test_url, params=params, json=data, headers=self.json_header, timeout=self.timeout)
        except Exception as e:
            return print('发生异常：%s' % e)

    def put_json(self, url, params, data):
        """定义put请求"""
        test_url = self.baseurl + url
        try:
            return requests.put(url=test_url, params=params, json=data, headers=self.json_header, timeout=self.timeout)
        except Exception as e:
            return print('发生异常：%s' % e)

    def post_file(self, url, params, data,files):
        """定义post请求"""
        test_url = self.baseurl + url
        try:
            return requests.post(url=test_url, params=params, data=data,files = files, headers=self.base_header, timeout=self.timeout)
        except Exception as e:
            return print('发生异常：%s' % e)

    def post_no_header(self, url, params, data):
        """定义post请求"""
        test_url = self.baseurl + url
        try:
            return requests.post(url=test_url, params=params, data=data, headers=self.base_header, timeout=self.timeout)
        except Exception as e:
            return print('发生异常：%s' % e)

    def put_no_header(self, url, params, data):
        """定义put请求"""
        test_url = self.baseurl + url

        try:
            return requests.put(url=test_url, params=params, data=data, headers=self.form_urlencoded_header, timeout=self.timeout)
        except Exception as e:
            return print('发生异常：%s' % e)










