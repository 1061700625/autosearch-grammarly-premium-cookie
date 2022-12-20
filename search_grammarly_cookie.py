import requests
from bs4 import BeautifulSoup
import json5
import pyperclip
from tqdm import tqdm
import time

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
        except TimeoutError: 
            print('>> 访问超时, 2s后切换下一个链接')
            time.sleep(2)
            continue
        content = soup.find('code', class_='language-json').string
        cookies.append(content)
    return cookies

def collect_cookies_xxxx():
    print('>> 当前搜索网站为: xxxx')
    cookies = []
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
    resp = requests.get(url, headers=headers ,allow_redirects=False)
    print(resp)
    return resp.status_code == 200

def user_define_collect_cookies():
    cookies = []
    user_define_functions = [collect_cookies_linkstricks, collect_cookies_xxxx]
    for functions in user_define_functions:
        cookies.extend(functions())
    return cookies

def search_valid_cookie():
    cookies = user_define_collect_cookies()
    print('>> 搜索完毕, 开始检查')
    for ck in cookies:
        if check_grammarly_cookie(str(ck)):
            try:
                pyperclip.copy(str(ck))
                print('>> 当前Cookie有效, 已复制到剪切板!')
            except Exception as e:
                print('>> 当前Cookie有效, 但复制到剪切板时失败: '+str(e))
            print('>> 也可手动复制该Cookie:')
            print(str(ck))
            return ck
    print('>> 该网站的Cookie均已失效')
    return None
##################################################################

print('>> 此工具来自【小锋学长生活大爆炸】, 欢迎使用! <<')
search_valid_cookie()

input('>> 欢迎下次使用, 输入任意键退出...')