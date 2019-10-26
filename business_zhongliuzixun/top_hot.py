import json
from base.net_post import NetPost
from business_zhongliuzixun import top_utils
from base import utils
from db import db_operate


# 肿瘤咨询-最热
class TopHot(NetPost):

    def handle_data(self, json_str):
        print(str(json_str))
        list_doc = json_str['docGroups'][0]['documents']
        data = list()
        for doc in list_doc:
            title = doc.get('title', '无标题')
            if utils.Utils.filter_content(title, top_utils.TopUtils.keys):
                doc['platform'] = '最热资讯'
                row = top_utils.TopUtils.change_dict(doc)
                data.append(row)
        return data

    # 公众号肿瘤咨询最新新闻
    def get_data_plugin(self, index, count):
        url = "http://www.liangyihui.net:8080//api/doc/gettoplist"
        data = {'filter': {'endTime': 0, 'pageIdx': index, 'pageSize': count, 'startTime': 0},
                'head': {'auth': '', 'auth2': '', 'cid': '', 'cver': '5.1', 'extensions': [{'name': '', 'value': ''}],
                         'sid': ''}, 'period': 0}
        header = {'content-type': "application/json;charset=UTF-8"}
        return self.get_data(url, json.dumps(data), header)


if __name__ == '__main__':
    hot = TopHot()
    datas = hot.get_data_plugin(0, 1000)
    # db_operate.DbOperator.insert(datas)
