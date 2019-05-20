from gongzhonghao.http_utils import HttpUtils
from gongzhonghao.wechat_login import WeChatLogin
from gongzhonghao.wechat_gongzhonghao import WeChatGongZhongHao
from gongzhonghao.wechat_gongzhonghao_content import WeChatContent
from db.db_info import DbInfo


# 抓取公众号的入口
class SpiderGZH(object):

    wechat_name = ''
    index = 0

    def __init__(self, name, index):
        self.wechat_name = name
        self.index = index

    def get_all_article(self):
        utils = HttpUtils()
        login = WeChatLogin()
        gzh = WeChatGongZhongHao()
        content = WeChatContent()

        # 登录自己订阅号 记录下cookie
        login.wechat_login()

        # 获取所有接口相关变量
        session = utils.get_session()
        header = utils.get_header()
        cookie = utils.get_cookies()
        token = utils.get_token(session, cookie)

        # 获取公众号列表的第一项
        fake_id = gzh.get_gongzhonghao(session, cookie, token, header, self.wechat_name, self.index)
        # 获取选定公众号的所有文章
        lists = content.get_content(token, fake_id, session, cookie, header)
        return lists

    def handle_data(self, datas):
        info_list = list()
        for data in datas:
            info = DbInfo()
            info.title = data.get('title')
            info.image = data.get('cover')
            info.image_urls = ''
            info.description = data.get('digest')
            info.source = '杨申淼'
            info.platform = '杨申淼'
            info.level = 2
            info.top = False
            info.url = data.get('link')
            info.type = '无'
            info.sub_title = data.get('digest')
            info_list.append(info)
        return info_list
