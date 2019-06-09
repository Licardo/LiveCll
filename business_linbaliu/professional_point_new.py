import json
from base.net_post import NetPost
from business_zhongliuzixun import top_utils
from base import utils
from db import db_operate
from db.db_info import DbInfo


# 肿瘤咨询-最热
class ProfessionalPointNew(NetPost):

    def handle_data(self, json_str):
        print(json_str['appmsg_list'])
        list_doc = json_str['appmsg_list']
        data = list()
        for doc in list_doc:
            title = doc.get('title', '无标题')
            if utils.Utils.filter_content(title, top_utils.TopUtils.keys):
                row = DbInfo()
                row.title = title
                row.sub_title = doc['digest']
                row.image = doc.get('cover', '无链接')
                row.image_urls = json.dumps(doc.get('picUrls', []))
                row.description = doc['digest']
                row.source = doc['author']
                row.platform = '专家说'
                row.level = 3
                row.top = False
                row.url = doc.get('link', '无链接')
                row.type = '无'
                if len(doc.get('labels', [])) > 0:
                    row.type = doc['labels'][0].get('name', '')
                data.append(row)
        return data

    # 公众号肿瘤咨询最新新闻
    def get_data_plugin(self,index, count):
        url = 'https://mp.weixin.qq.com/mp/homepage?__biz=MjM5ODcyNTMyMA==&hid=4&sn=bd1eaf83f35bcc715280b1121aa48284&' \
              'cid=0&begin=%d&count=%d&action=appmsg_list&f=json&r=0.028248694732190494&appmsg_token=' % (index, count)
        data = {'__biz': 'MjM5ODcyNTMyMA==', 'hid': '4', 'sn': 'bd1eaf83f35bcc715280b1121aa48284',
                'cid': '0', 'begin': index, 'count': count, 'action': 'appmsg_list',
                'f': 'json', 'r': '0.7171119548643772', 'appmsg_token': ''}
        header = {'Accept': 'application/json',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9',
                  'Content-Length': '0',
                  'Connection': 'keep-alive',
                  'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
                  'Referer': 'https://mp.weixin.qq.com/mp/homepage?__biz=MjM5ODcyNTMyMA==&hid=4&sn=bd1eaf83f35bcc715280b1121aa48284',
                  'Host': 'mp.weixin.qq.com',
                  'X-Requested-With': 'XMLHttpRequest'}
        return self.get_data(url, json.dumps(data), header)


if __name__ == '__main__':
    hot = ProfessionalPointNew()
    datas = hot.get_data_plugin(0, 100)
    print(len(datas))
    db_operate.DbOperator.insert(datas)
