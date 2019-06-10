from bmob import bmob
import json
from base.net_get import NetGet


class OperateData:

    def get_datas(self, page_min, page_max):
        net = NetGet()
        url = 'http://0.0.0.0:8000/todo/list/get_item/%d/%d' % (page_min, page_max)
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
            # vos.append(vo)
            b.insert('cll_data', vo)

    def update(self):
        b = bmob.Bmob('3342bfd2beedca7937a33146715c93df', 'e37c4f58e5320b6dca4101ebe22da944')
        resonse = b.find("cll_data", {'source': '淋巴瘤之家'})
        # print(resonse.jsonData)
        for item in resonse.jsonData['results']:
            vo = dict()
            vo['platform'] = item['platform']
            vo['title'] = item['title']
            vo['sub_title'] = item['sub_title']
            vo['url'] = item['url']
            vo['image'] = 'https://mmbiz.qpic.cn/mmbiz_png/y4URaX8bynKPg1LBzX26LkBib8pIGuadgEUV24AhlvjxzJub5KbvOHEFgthL6Z8obupfofKG8PeWov5rpFSfavA/640?wx_fmt=png&amp;tp=webp&amp;wxfrom=5&amp;wx_lazy=1&amp;wx_co=1'
            vo['image_urls'] = item['image_urls']
            vo['description'] = item['description']
            vo['source'] = item['source']
            vo['level'] = item['level']
            vo['top'] = item['top']
            vo['type'] = item['type']
            b.update('cll_data', item['objectId'], vo)
            pass


if __name__ == '__main__':
    ope = OperateData()
    # for i in range(30):
    #     ope.insert(ope.get_datas(i))
    # ope.update()
    ope.insert(ope.get_datas(193, 242))
