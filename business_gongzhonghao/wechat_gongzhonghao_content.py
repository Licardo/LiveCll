import random
import requests

class WeChatContent:
    def get_content(self, token, fakeid, session, cookies, header):
        # 获取公众号文章接口
        article_url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?'
        begin = 0
        query_id_data = {
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'action': 'list_ex',
            'begin': '0',  # 不同页，此参数变化，变化规则为每页加5
            'count': '5',
            'query': '',
            'fakeid': fakeid,
            'type': '9'
        }
        article_response = session.get(article_url, cookies=cookies, headers=header, params=query_id_data)
        max_num = article_response.json().get('app_msg_cnt')
        num = int(int(max_num) / 5)

        contents = list()
        while num + 1 > 0:
            query_id_data = {
                'token': token,
                'lang': 'zh_CN',
                'f': 'json',
                'ajax': '1',
                'random': random.random(),
                'action': 'list_ex',
                'begin': '{}'.format(str(begin)),  # 不同页，此参数变化，变化规则为每页加5
                'count': '5',
                'query': '',
                'fakeid': fakeid,
                'type': '9'
            }
            query_fakeid_response = requests.get(article_url, cookies=cookies, headers=header, params=query_id_data)
            print('-----------------杨申淼-------------------')
            print(str(query_fakeid_response.json()))
            fakeid_list = query_fakeid_response.json().get('app_msg_list')
            contents.extend(fakeid_list)
            num -= 1
            begin = int(begin)
            begin += 5

        return contents
