import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from base.net_post import NetPost
from base import pf_excel
from base import utils
from zhongliuzixun import top_utils


class TopLatest(NetPost):
    # 输出目录
    out_dir = '../product/latest.txt'

    # 公众号肿瘤咨询最新新闻
    def get_data_plugin(self, index):
        url = "http://www.liangyihui.net:8080//api/doc/getdocumentlist"
        data = {'filters': [{'items': [{'filterId': "1", 'type': 1}], 'filterGroupId': 1}], 'head': {
            'cid': "", 'cver': "", 'sid': "", 'extensions': [{'name': "", 'value': ""}], 'auth': "", 'auth2': ""},
                'sort': {'pageIdx': index, 'pageSize': 30, 'startTime': 0}}
        header = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}
        return self.get_data(url, json.dumps(data), header)

    # todo 抽象方法 父类会有声明
    # 网络数据处理逻辑
    def handle_data(self, req_json):
        list_doc = req_json['docGroups'][0]['documents']
        data = []
        for doc in list_doc:
            title = doc.get('title', '无标题')
            if utils.Utils.filter_content(title, top_utils.TopUtils.keys):
                row = top_utils.TopUtils.change_dict(doc)
                data.append(row)
                # print(rows[0] + '\t' + rows[1])
                with open(self.out_dir, 'a', encoding='utf-8') as file:
                    file.write(str(row) + '\r\n')
        return data

    # 循环获取多页数据
    def loop_data(self, size):
        open(self.out_dir, 'w')
        datas = []
        for i in range(size):
            data = self.get_data_plugin(i)
            datas.extend(data)
        # pf_excel.Excel.write_excel(datas, 'paofan')
        print(datas)
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        return datas

    # 定时服务 每天每小时执行一次
    def schedule_timer(self):
        schedule = BlockingScheduler()
        # 每天16-18点的0-4分钟执行 执行频率是5秒钟
        schedule.add_job(func=self.loop_data, args=(30,), trigger='cron', month='1-12', day='1-31', hour='*/1')
        # 每五秒执行一次
        # schedule.add_job(func=loop_data, args=(1,), trigger='interval', seconds=5)
        schedule.start()


if __name__ == '__main__':
    # schedule_timer()
    top = TopLatest()
    top.loop_data(30)
