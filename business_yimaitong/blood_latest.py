from base import utils
from base.net_post import NetPost
from business_zhongliuzixun import top_utils


class Blood(NetPost):

    def handle_data(self, json_str):
        print(json_str['data_list'].__len__())
        print(json_str)
        infos = json_str['data_list']
        data = []
        for info in infos:
            if utils.Utils.filter_content(info['title'], top_utils.TopUtils.keys):
                doc = {'title': info['title'], 'platform': info['copyfrom'], 'picUrl': info['thumb'], 'picUrls': [],
                       'documentDetailUrl': info['url'], 'releaseTime': info['updatetime']}
                row = top_utils.TopUtils.change_dict(doc)
                row.description = info['description']
                row.source = info['copyfrom']
                row.type = info['type']
                data.append(row)
        return data

    def get_data_plugin(self, index):
        url = "https://m.medlive.cn/cms/ajax/cms_load_more.ajax.php"
        header = {'content-type': "application/x-www-form-urlencoded",
                  'content-length': "50",
                  'authority': "m.medlive.cn",
                  'sec-fetch-site': "same-origin",
                  'sec-fetch-mode': "cors"
                  }
        params = {'start': index, 'branch': '7', 'cat': 'research'}
        return self.get_data(url, params, header)


if __name__ == '__main__':
    blood = Blood()
    blood.get_data_plugin(0)
