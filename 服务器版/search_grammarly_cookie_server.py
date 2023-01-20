import requests
from bs4 import BeautifulSoup
import json5
import json
import pyperclip
from tqdm import tqdm
import time
import shutil
import os

##################################################################
def cookie_convert_j2s(cookie_json):
    str_json = ''
    for item in cookie_json:
        str_json += f'{item["name"]}={item["value"]}; '
    return str_json
##################################################################

##################################################################
def collect_cookies_linkstricks():
    print('>> 当前搜索网站为: linkstricks')
    cookies = []
    for i in tqdm(range(1, 7), desc='搜索中...'):
        url = f'https://www.linkstricks.com/grammarly-cookies-{i}/'
        try:
            soup = BeautifulSoup(requests.get(url, timeout=10).text, 'lxml')
        except: 
            print('>> 访问超时, 2s后切换下一个链接')
            time.sleep(2)
            continue
        content = soup.find('code', class_='language-json').string
        cookies.append(content)
    return cookies

def collect_cookies_trytechnical():
    print('>> 当前搜索网站为: trytechnical')
    cookies = []
    for i in tqdm(range(1, 4), desc='搜索中...'):
        url = f'https://trytechnical.com/working-grammarly-cookies-hourly-updated-{i}/'
        try:
            soup = BeautifulSoup(requests.get(url, timeout=10).text, 'lxml')
        except: 
            print('>> 访问超时, 2s后切换下一个链接')
            time.sleep(2)
            continue
        content = soup.find('pre', class_='wp-block-preformatted').string
        cookies.append(content)
    return cookies

def collect_cookies_infokik():
    print('>> 当前搜索网站为: infokik')
    cookies = []
    for i in tqdm(range(1, 5), desc='搜索中...'):
        url = f'https://infokik.com/grammarly-{i}/'
        try:
            soup = BeautifulSoup(requests.get(url, timeout=10).text, 'lxml')
        except: 
            print('>> 访问超时, 2s后切换下一个链接')
            time.sleep(2)
            continue
        content = soup.find('pre', class_='wp-block-code').string
        cookies.append(content)
    return cookies

def collect_cookies_xxxx():
    print('>> 当前搜索网站为: xxxx')
    cookies = []
    # xxxxxxxxxxxxxxx
    # your code
    # xxxxxxxxxxxxxxx
    return cookies
##################################################################

##################################################################
def check_grammarly_cookie(cookie):
    url = 'https://app.grammarly.com/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'cookie': cookie_convert_j2s(json5.loads(cookie))
    }
    retry_cnt = 0
    retry_max = 5
    while retry_cnt < retry_max:
        try:
            resp = requests.get(url, headers=headers, allow_redirects=False)
            print(resp)
            return resp.status_code == 200
        except:
            retry_cnt += 1
            print(f'失败, 1s后重试...{retry_cnt}/{retry_max}')
            time.sleep(1)
    return False

def user_define_collect_cookies():
    cookies = []
    user_define_functions = [collect_cookies_linkstricks, collect_cookies_trytechnical, collect_cookies_infokik, collect_cookies_xxxx]
    for functions in user_define_functions:
        cookies.extend(functions())
    return cookies

def search_valid_cookie():
    cookies = user_define_collect_cookies()
    print('>> 搜索完毕, 开始检查')
    if os.path.exists('./cookies'):
        print('>> 先清空一下cookies目录')
        shutil.rmtree('./cookies')
    os.mkdir('./cookies')
    ck_file_store = []
    for i, ck in enumerate(cookies):
        if check_grammarly_cookie(str(ck)):
            print(f'>> 当前Cookie[{i}]有效!')
            ck_file_store.append(f"./cookies/cookie-{i}.json")
            with open(f"./cookies/cookie-{i}.json","w+") as f:
                json.dump(json5.loads('{"ck":' + ck + '}'), f)
                print("写入json文件完成")
    print('>> 该网站的Cookie均已失效')
    with open(f"./cookies/cookies.txt","w+") as f:
        f.write('\n'.join(ck_file_store))
        print("写入list文件完成")
##################################################################

# ------------------------Test------------------------------- #
# res = collect_cookies_trytechnical()
# res = collect_cookies_infokik()
# print(res[0])
# exit()
# ------------------------Test------------------------------- #

print('>> 此工具来自【小锋学长生活大爆炸】, 欢迎使用! <<')
print('>> 此工具仅做学习交流，请勿用于非法用途!! <<')
print('>> 请不要手动点击“退出登录”，以免Cookie失效，损人不利己!!! <<')
print()

while True:
    search_valid_cookie()
    print(f'>> 完成一次，间隔10分钟[{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}]')
    time.sleep(60*10)

print('>> 欢迎下次使用')
input('>> 输入任意键退出...')


