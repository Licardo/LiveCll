from base.net_post import NetPost
import requests


class Blood(NetPost):

    def handle_data(self, json_str):
        print(str(json_str))

    # 公众号肿瘤咨询最新新闻
    def get_data_plugin(self):
        url = "https://m.medlive.cn/cms/ajax/cms_load_more.ajax.php"
        header = {'content-type': "application/x-www-form-urlencoded",
                  # 'sec-ch-ua': "'Google Chrome';v='89', 'Chromium';v='89', ';Not A Brand';v='99'",
                  # 'user-agent': "Chrome/172.16.20.105",
                  # 'accept-encoding': "gzip, deflate, br",
                  # 'referer': "https://m.medlive.cn/branch/researchlist/7?_wx=1",
                  # 'accept': "application/json, text/javascript, */*; q=0.01",
                  'content-length': "50",
                  'authority': "m.medlive.cn",
                  'sec-fetch-site': "same-origin",
                  'sec-fetch-mode': "cors"
                  }
        req = requests.post(url, data={'start': 0, 'branch': '7', 'cat': 'research'}, headers=header)
        print(str(req.json()))


if __name__ == '__main__':
    blood = Blood()
    blood.get_data_plugin()
