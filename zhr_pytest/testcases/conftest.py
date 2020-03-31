import pytest
import requests
import json
from py._xmlgen import html
from common import env_config
import datetime


driver = None
projectName = " isc-dmp-lib API-Test"
# 获取UTC时间
timeUTC = datetime.datetime.utcnow()
# 将UTC时间转换成东8区时间
nowTime = time_now = (timeUTC + datetime.timedelta(hours=8))

weChatSwitch = env_config.switch()
jenkinsBuildNumber = env_config.getBuildNumber()


report_result = {
    'passed': 0,
    'skipped': 0,
    'failed': 0,
    'rerun': 0,
}
run_dict = {}


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    pytest_html = item.config.pluginmanager.getplugin('html')

    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    extra.append(pytest_html.extras.text('some string', name='Different title'))
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码

    if report.when == 'call':
        # 查看这个任务是否已经跑过了
        if report.nodeid in run_dict:
            # 已经跑过了
            report_result['rerun'] += 1
            # 本次如果成功了，说明重跑成功了
            if report.passed:
                report_result['failed'] -= 1
                report_result['passed'] += 1
        else:
            # 标记已经跑过了
            run_dict[report.nodeid] = 1
            if report.passed:
                report_result['passed'] += 1
            else:
                report_result['failed'] += 1

    else:
        if report.skipped:
            report_result['skipped'] += 1


def pytest_configure(config):
    # 添加接口地址与项目名称
    config._metadata["项目名称"] = projectName











