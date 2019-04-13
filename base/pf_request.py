import requests
import json
from abc import abstractmethod, ABC


class NetBase(ABC):
    # 发起post请求
    def post(self, url, param, header, stream=True):
        if type(param) == dict:
            data = json.dump(param)
        elif type(param) == str:
            data = param
        req = requests.post(url, data=data, headers=header)
        return req

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

    # todo 抽象到底层
    # 发起网络请求 可以抽象出来 跟业务隔离
    def get_data(self, url, param, head):
        req = self.post(url, param, head, stream=True)
        if req.status_code == 200 and req.content:
            try:
                req_json = req.json()
                return self.handle_data(req_json)
            except json.decoder.JSONDecodeError:
                with open('exception.txt', 'a+') as file:
                    file.write(req.status_code + '\n' + req.content)

    # 抽象方法 子类会实现该方法
    @abstractmethod
    def handle_data(self, json_str):
        pass
