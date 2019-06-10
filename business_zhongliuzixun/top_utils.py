import json
from db import db_info


class TopUtils:
    keys = ['淋巴瘤', '慢淋', 'CLL', '李建勇', '杨申淼', '邱录贵', 'FCR', '伊布替尼', '靶向药', 'CAR-T', '慢性淋巴细胞白血病',
            'MD安德森', '流式', 'FISH', '霍奇金', '百济神州', '泽布替尼', 'CD20', '利妥昔单抗', '氟达拉滨']

    @staticmethod
    def change_dict(doc):
        row = db_info.DbInfo()
        row.title = doc.get('title', '无标题')
        row.image = doc.get('picUrl', '无链接')
        row.image_urls = json.dumps(doc.get('picUrls', []))
        row.description = ''
        row.source = '肿瘤资讯'
        row.platform = doc.get('platform', "最新资讯")
        row.level = 3
        row.top = False
        row.url = doc.get('documentDetailUrl', '无链接')
        row.type = '无'
        row.sub_title = ''
        if len(doc.get('channels', [])) > 0:
            row.sub_title = doc['channels'][0]['name']
        if len(doc.get('labels', [])) > 0:
            row.type = doc['labels'][0].get('name', '')
        return row
