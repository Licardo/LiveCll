import time
import re
import requests
import json

class HttpUtils:
    def get_token(self, session, cookies):
        url = 'https://mp.weixin.qq.com'
        import urllib3
        # 关闭警告
        urllib3.disable_warnings()

        time.sleep(5)
        response = session.get(url=url, cookies=cookies, verify=False)
        token = re.findall(r'token=(\d+)', str(response.url))[0]
        return token

    def get_session(self):
        session = requests.Session()
        session.keep_alive = False
        session.adapters.DEFAULT_RETRIES = 511
        return session

    def get_cookies(self):
        with open('cookie.txt', 'r', encoding='utf-8') as f:
            cookie = f.read()
        cookies = json.loads(cookie)
        return cookies

    def get_header(self):
        header = {
            "HOST": "mp.weixin.qq.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"

        }
        return header