from bmob import bmob
import json
from base.net_get import NetGet


class OperateData:

    def get_datas(self, page_min, page_max):
        net = NetGet()
        url = 'http://172.21.0.16:8000/todo/list/get_item/%d/%d' % (page_min, page_max)
        str_json = net.get(url)
        jsons = json.loads(str_json)
        return jsons

    def insert(self, jsons):
        b = bmob.Bmob('3342bfd2beedca7937a33146715c93df', 'e37c4f58e5320b6dca4101ebe22da944')
        # vos = list()
        if jsons is None:
            return
        for j in jsons:
            vo = dict()
            vo['title'] = j[1]
            vo['sub_title'] = j[2]
            vo['url'] = j[3]
            vo['image'] = j[4]
            vo['image_urls'] = j[5]
            vo['description'] = j[6]
            vo['source'] = j[7]
            vo['platform'] = j[8]
            vo['level'] = j[9]
            vo['top'] = j[10]
            vo['type'] = j[11]
            vo['send_time'] = j[12]
            # vos.append(vo)
            b.insert('cll_data', vo)

    def update(self, jsons):
        b = bmob.Bmob('3342bfd2beedca7937a33146715c93df', 'e37c4f58e5320b6dca4101ebe22da944')
        resonse = b.find("cll_data", limit=200, skip=400)
        # print(resonse.jsonData)
        for item in resonse.jsonData['results']:
            for j in jsons:
                if item['url'] == j[3]:
                    vo = dict()
                    vo['send_time'] = j[12]
                    b.update('cll_data', item['objectId'], vo)
                    break
            pass


if __name__ == '__main__':
    ope = OperateData()
    # for i in range(30):
    #     ope.insert(ope.get_datas(i))
    # ope.update()
    ope.insert(ope.get_datas(193, 242))
