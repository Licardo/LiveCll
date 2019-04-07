from json import JSONDecodeError

import requests
import json
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import pandas as pd


# 公众号肿瘤咨询最新新闻
def get_data(index):
    url = "http://www.liangyihui.net:8080//api/doc/getdocumentlist"
    data = {'filters':[{'items': [{'filterId': "1", 'type': 1}], 'filterGroupId': 1}], 'head':{'cid': "", 'cver': "", 'sid': "", 'extensions': [{'name': "", 'value': ""}], 'auth': "", 'auth2': ""},'sort':{'pageIdx': index, 'pageSize': 30, 'startTime': 0}}
    req = requests.post(url, data=json.dumps(data), stream=True, headers={'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'})
    list_doc = []
    if req.status_code == 200 and req.content:
        req_json = None
        try:
            req_json = req.json()
        except json.decoder.JSONDecodeError:
            with open('exception.txt', 'a+') as file:
                file.write(req.status_code + '\n' + req.content)
        list_doc = req_json['docGroups'][0]['documents']
    data = []
    for doc in list_doc:
        rows = list()
        rows.append(doc.get('title', '无标题'))
        rows.append(doc.get('documentDetailUrl', '无链接'))
        data.append(rows)
        print(rows[0] + '\t' + rows[1])
        with open('latest.txt', 'a', encoding='utf-8') as file:
            file.write(rows[0] + '\t' + rows[1] + '\r\n')
    return data


def operate_excel(excel_datas, name):
    df = pd.DataFrame(data=excel_datas)
    write = pd.ExcelWriter('latest.xls')
    df.to_excel(write, sheet_name=name, index=None)
    write.save()
    write.close()
    print(df)


def loop_data(size):
    open('latest.txt', 'w')
    datas = []
    for i in range(size):
        data = get_data(i)
        datas.extend(data)
    # operate_excel(datas, 'paofan')
    print(time.strftime('%Y-%m-%D %H:%M:%S', time.localtime()))


def schedule_timer():
    sche = BlockingScheduler()
    # 每天16-18点的0-4分钟执行 执行频率是5秒钟
    sche.add_job(func=loop_data, args=(30,), trigger='cron', month='1-12',
                 day='1-31', hour='*/1')
    # 每五秒执行一次
    # sche.add_job(func=loop_data, args=(1,), trigger='interval', seconds=5)
    sche.start()


if __name__ == '__main__':
    schedule_timer()
    # loop_data(30)
