import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from base.net_post import NetPost
from base import pf_excel
from base import utils
from business_zhongliuzixun import top_utils


# 肿瘤咨询-最新
class TopLatest(NetPost):
    # 输出目录
    out_dir = '../product/latest.txt'
    page_index = 0
    page_count = 15
    is_stop = False
    MAX_INDEX = 50

    # todo 抽象方法 父类会有声明
    # 网络数据处理逻辑
    def handle_data(self, req_json):
        # print(str(req_json))
        print(str(self.page_index))
        self.page_index += 1
        data = []
        if req_json is None or req_json['docGroups'] is None or len(req_json['docGroups']) < 1:
            return data
        list_doc = req_json['docGroups'][0]['documents']
        for doc in list_doc:
            title = doc.get('title', '无标题')
            if utils.Utils.filter_content(title, top_utils.TopUtils.keys):
                doc['platform'] = '最新资讯'
                row = top_utils.TopUtils.change_dict(doc)
                data.append(row)
                print(title)
                # print(rows[0] + '\t' + rows[1])
                # with open(self.out_dir, 'a', encoding='utf-8') as file:
                #     file.write(str(row) + '\r\n')
        if len(list_doc) < self.page_count or self.page_index >= self.MAX_INDEX:
            self.is_stop = True
        else:
            self.get_all_data()
        return data

    def get_all_data(self):
        url = "https://api.liangyihui.net//api/doc/getdocumentlist"

        # data = {'filters': [{'items': [{'filterId': "1", 'type': 1}], 'filterGroupId': 1}], 'head': {
        #     'cid': "", 'cver': "", 'sid': "", 'extensions': [{'name': "", 'value': ""}], 'auth': "", 'auth2': ""},
        #         'sort': {'pageIdx': self.pageIdx, 'pageSize': 30, 'startTime': 0}}

        data = {"filters": [{"filterGroupId": 1, "items": [{"filterId": 1, "type": 1}]}],
                "head": {"auth": "", "auth2": "", "cid": "354782065344066", "cver": "3.3", "extensions": []},
                "path": "/api/doc/getdocumentlist", "sort": {"pageIdx": self.page_index, "pageSize": self.page_count,
                                                             "startTime": 0}}

        header = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}
        if not self.is_stop:
            return self.get_data(url, json.dumps(data), header)

    # # 定时服务 每天每小时执行一次
    # def schedule_timer(self):
    #     schedule = BlockingScheduler()
    #     # 每天16-18点的0-4分钟执行 执行频率是5秒钟
    #     schedule.add_job(func=self.loop_data, args=(30,), trigger='cron', month='1-12', day='1-31', hour='*/1')
    #     # 每五秒执行一次
    #     # schedule.add_job(func=loop_data, args=(1,), trigger='interval', seconds=5)
    #     schedule.start()


if __name__ == '__main__':
    # schedule_timer()
    top = TopLatest()
    top.get_all_data()
