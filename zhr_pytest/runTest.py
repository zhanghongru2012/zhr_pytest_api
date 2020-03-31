#!/usr/bin/env python 
# -*- coding:utf-8 -*-
_author_ = 'zhanghr'
import pytest


if __name__ == "__main__":
    '''30秒后重跑5次'''
    test_result = pytest.main([
        "--html=./report/report.html",
        "--self-contained-html",
        "--alluredir=./report/allure-results",
        "-s",
        "--clean-alluredir"])
    if test_result != 0:
        exit(1)

