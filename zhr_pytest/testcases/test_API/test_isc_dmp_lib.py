#!/usr/bin/env python
# -*- coding:utf-8 -*-
_author_ = 'zhanghr'
from common import requestMethod
import pytest
import logging


class Test_class_isc_dmp_lib():
    '''isc-dmp-lib'''

    # def test_post_iscdmp_api_dmp_login(self):
    #     '''登录获取Set_Cookie'''
    #
    #     url = '/api/phoenix/cloud/authentication/login'
    #     query={
    #     }
    #     data = {
    #         # 用户名
    #         'loginName': 'user',
    #         'password': '123456'
    #         # 密码
    #     }
    #     # multipart/form-data
    #     self.result = requestMethod.RequestMethod().post(url, query, data)
    #     # 打印当前Set-Cookie
    #     # print(self.result['Set_Cookie'])
    #     # object
    #     logging.info('接口返回结果： %s' % self.result.text)
    #     assert self.result.status_code == 200

    def test_post_isc_dmp_api_dmp_sub_system(self):
        '''添加子系统'''
        
        url = '/isc-dmp/api/dmp/sub-system'
        query = {
        }
        data = {
             # formData - string - 子系统名
            'name': 'zhr_test',
             # formData - string - 描述
            'description': '',
             # formData - string - 父id
            'parentId': '',
        }
        # multipart/form-data
        self.result = requestMethod.RequestMethod().post_no_header(url, query, data)
        # object
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200 or 400

    def test_delete_isc_dmp_api_dmp_sub_system(self):
        '''删除子系统'''
        
        url = '/isc-dmp/api/dmp/sub-system/{id}'
        query = {
        }
        id = 2
        url = url.replace('{id}', str(id))
        # multipart/form-data
        self.result = requestMethod.RequestMethod().delete(url, query)
        # unknown
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_get_isc_dmp_api_dmp_sub_system(self):
        '''分页获取子系统'''
        
        url = '/isc-dmp/api/dmp/sub-system'
        query = {
             # query - string - 当前页，默认1
            'current': '1',
             # query - string - 每页条数，默认10
            'size': '10',
             # query - string - 关键词
            'keyword': '',
             # query - string - 父id
            'parentId': '',
        }
        
        # unknown
        self.result = requestMethod.RequestMethod().get(url, query)
        # object
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_put_isc_dmp_api_dmp_sub_system(self):
        '''编辑子系统'''
        
        url = '/isc-dmp/api/dmp/sub-system'
        query = {
        }
        data = {
             # formData - string - 子系统id
            'id': 1,
             # formData - string - 子系统名
            'name': 'zhr',
             # formData - string - 子系统描述
            'description': '',
             # formData - string - 父id
            'parentId': '',
        }
        # multipart/form-data
        self.result = requestMethod.RequestMethod().put_no_header(url, query, data)
        # unknown
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_get_iscdmp_api_dmp_product(self):
        '''分页获取产品'''
        
        url = '/isc-dmp/api/dmp/product'
        query = {
             # query - string - 当前页，默认1
            'current': '1',
             # query - string - 每页条数，默认10
            'size': '10',
             # query - string - 查询关键词
            'keyword': '',
        }
        
        # unknown
        self.result = requestMethod.RequestMethod().get(url, query)
        print(self.result.status_code)
        # object
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_delete_iscdmp_api_dmp_product(self):
        '''删除产品'''
        url = '/isc-dmp/api/dmp/product/{id}'
        id = 1
        query = {
        }
        url = url.replace('{id}', str(id))
        # multipart/form-data
        self.result = requestMethod.RequestMethod().delete(url, query)
        # unknown
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_post_iscdmp_api_dmp_product(self):
        '''添加产品'''
        
        url = '/isc-dmp/api/dmp/product'
        query = {
        }
        data = {
             # formData - string - 产品名称
            'name': 'zhr',
            # 'name': '1',  # 尝试产品名称不包含字符串时是否能够创建成功
             # formData - string - 产品类型id
            'subSystemId': '1',
             # formData - string - 产品描述
            'description': '',
             # formData - string - 驱动id
            'driverId': '1',
             # formData - string - 品牌
            'brand': 'qwe',
             # formData - string - 型号
            'model': 'qwe',
        }
        # multipart/form-data
        self.result = requestMethod.RequestMethod().post_no_header(url, query, data)
        # object
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200 or 400

    def test_put_iscdmp_api_dmp_product(self):
        '''编辑产品'''
        
        url = '/isc-dmp/api/dmp/product'
        query = {
        }
        data = {
             # formData - string - 产品id
            'id': '1',
             # formData - string - 产品名称
            'name': 'zzz',
            # 'name': '1', # 尝试产品名称不包含字符串时是否能够创建成功
             # formData - string - 产品类型id
            'subSystemId': '1',
             # formData - string - 产品描述
            'description': '',
             # formData - string - 驱动id
            'driverId': '1',
             # formData - string - 品牌
            'brand': '1',
             # formData - string - 型号
            'model': '1',
        }
        # multipart/form-data
        self.result = requestMethod.RequestMethod().put_no_header(url, query, data)
        # unknown
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_get_iscdmp_api_dmp_product_id(self):
        '''获取单个产品'''
        # 产品id
        id = '1'
        url = '/isc-dmp/api/dmp/product/{id}'
        query = {
        }
        url = url.replace('{id}', str(id))
        
        # unknown
        self.result = requestMethod.RequestMethod().get(url, query)
        # object
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_get_iscdmp_api_dmp_subSystem_id(self):
        '''获取单个子系统'''
        # 子系统id
        id = 2
        url = '/isc-dmp/api/dmp/sub-system/{id}'
        query = {
        }
        url = url.replace('{id}', str(id))
        
        # unknown
        self.result = requestMethod.RequestMethod().get(url, query)
        # object
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_get_iscdmp_api_dmp_driver_desc(self):
        '''获取驱动描述'''
        
        url = '/isc-dmp/api/dmp/driver/desc'
        query = {
             # query - string - 驱动id
            'driverId': 'asdfgh',
        }
        
        # unknown
        self.result = requestMethod.RequestMethod().get(url, query)
        # object
        logging.info('接口返回结果：%s' % self.result.text)
        assert self.result.status_code == 200

    def test_get_isc_dmp_api_dmp_driver_get_properties(self):
        '''获取驱动属性列表'''

        url = '/isc-dmp/api/dmp/driver/get-properties'
        query = {
            # query - string - 驱动id
            'driverId': 'asdfgh',
        }
        self.result = requestMethod.RequestMethod().get(url, query)
        logging.info('接口返回结果' % self.result.text)
        assert self.result.status_code == 200

    def test_isc_dmp_api_dmp_driver_get_events(self):
        '''获取驱动事件列表'''

        url = '/isc-dmp/api/dmp/driver/get-events'
        query = {
            # query - string - 驱动id
            'driverId': 'asdfgh',
        }
        self.result = requestMethod.RequestMethod().get(url, query)
        logging.info('接口返回结果' % self.result.text)
        assert self.result.status_code == 200

    def test_isc_dmp_api_dmp_driver_get_services(self):
        '''获取驱动服务列表'''

        url = '/isc-dmp/api/dmp/driver/get-services'
        query = {
            # query - string - 驱动id
            'driverId': 'asdfgh',
        }
        self.result = requestMethod.RequestMethod().get(url, query)
        logging.info('接口返回结果' % self.result.text)
        assert self.result.status_code == 200



# a = Test_class_0()
# a.test_get_iscdmp_api_dmp_product()
