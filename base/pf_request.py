import requests
import json


# 发起post请求
def post(url, param, header):
    if type(param) == dict:
        data = json.dump(param)
    elif type(param) == str:
        data = param
    req = requests.post(url, data=data, headers=header)
    return req.json()


# 发起get请求
def get(url, param=None, header=None):
    if param is None:
        data = None
    elif type(param) == dict:
        data = json.dump(param)
    elif type(param) == str:
        data = param
    req = requests.get(url, params=data, headers=header)
    return req.json()
