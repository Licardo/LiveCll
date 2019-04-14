import requests
import json


class NetGet(object):
    # 发起get请求
    def get(self, url, param=None, header=None):
        if param is None:
            data = None
        elif type(param) == dict:
            data = json.dump(param)
        elif type(param) == str:
            data = param
        req = requests.get(url, params=data, headers=header)
        return req.json()
