import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
from base import pf_request
from base import pf_excel

# 输出目录
out_dir = 'product/latest.txt'


# 公众号肿瘤咨询最新新闻
def get_data_plugin(index):
    url = "http://www.liangyihui.net:8080//api/doc/getdocumentlist"
    data = {'filters':[{'items': [{'filterId': "1", 'type': 1}], 'filterGroupId': 1}], 'head':{'cid': "", 'cver': "", 'sid': "", 'extensions': [{'name': "", 'value': ""}], 'auth': "", 'auth2': ""},'sort':{'pageIdx': index, 'pageSize': 30, 'startTime': 0}}
    header = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}
    return get_data(url, json.dumps(data), header)


# todo 抽象到底层
# 发起网络请求 可以抽象出来 跟业务隔离
def get_data(url, param, head):
    req = pf_request
    req = req.post(url, param, head, stream=True)
    if req.status_code == 200 and req.content:
        try:
            req_json = req.json()
            return handle_data(req_json)
        except json.decoder.JSONDecodeError:
            with open('exception.txt', 'a+') as file:
                file.write(req.status_code + '\n' + req.content)


# 网络数据处理逻辑
def handle_data(req_json):
    list_doc = req_json['docGroups'][0]['documents']
    data = []
    for doc in list_doc:
        rows = list()
        rows.append(doc.get('title', '无标题'))
        rows.append(doc.get('documentDetailUrl', '无链接'))
        data.append(rows)
        print(rows[0] + '\t' + rows[1])
        with open(out_dir, 'a', encoding='utf-8') as file:
            file.write(rows[0] + '\t' + rows[1] + '\r\n')
    return data


# 循环获取多页数据
def loop_data(size):
    open(out_dir, 'w')
    datas = []
    for i in range(size):
        data = get_data_plugin(i)
        datas.extend(data)
    # pf_excel.Excel.write_excel(datas, 'paofan')
    print(time.strftime('%Y-%m-%D %H:%M:%S', time.localtime()))
    return datas


# 定时服务 每天每小时执行一次
def schedule_timer():
    schedule = BlockingScheduler()
    # 每天16-18点的0-4分钟执行 执行频率是5秒钟
    schedule.add_job(func=loop_data, args=(30,), trigger='cron', month='1-12', day='1-31', hour='*/1')
    # 每五秒执行一次
    # schedule.add_job(func=loop_data, args=(1,), trigger='interval', seconds=5)
    schedule.start()


if __name__ == '__main__':
    # schedule_timer()
    loop_data(1)
