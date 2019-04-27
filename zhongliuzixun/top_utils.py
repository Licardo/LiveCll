import json


class TopUtils:
    keys = ['淋巴瘤', '慢淋', 'CLL', '李建勇', '杨申淼', '邱录贵', 'FCR', '伊布替尼', '靶向药', 'CAR-T']

    @staticmethod
    def change_dict(doc):
        row = dict()
        row['title'] = doc.get('title', '无标题')
        row['image'] = doc.get('picUrl', '无链接')
        row['image_urls'] = json.dumps(doc.get('picUrls', []))
        row['description'] = ''
        row['source'] = '最新资讯'
        row['platform'] = '肿瘤资讯'
        row['level'] = 3
        row['top'] = False
        row['url'] = doc.get('documentDetailUrl', '无链接')
        row['type'] = '无'
        row['sub_title'] = ''
        if len(doc.get('channels', [])) > 0:
            row['sub_title'] = doc['channels'][0]['name']
        if len(doc.get('labels', [])) > 0:
            row['type'] = doc['labels'][0].get('name', '')
        return row
