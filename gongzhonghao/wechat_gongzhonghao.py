import random


class WeChatGongZhongHao:

    def get_gongzhonghao(self, session, cookies, token, header, name, index):
        search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
        query_id = {
            'action': 'search_biz',
            'token': token,
            'lang': 'zh_CN',
            'f': 'json',
            'ajax': '1',
            'random': random.random(),
            'query': name,
            'begin': '0',
            'count': '5'
        }
        search_response = session.get(search_url, cookies=cookies, headers=header, params=query_id)
        print(str(search_response.json()))
        lists = search_response.json().get('list')[index]
        fakeid = lists.get('fakeid')
        return fakeid


