from server.tab_info import TabInfo
from server.tab_info import TabChildInfo
from server.home_info import HomeTitle
from server.home_info import HomeContent
from server.cll_info import CllInfo
from db import db_base


class CllDB:
    @staticmethod
    def get_tab_info():
        sql = 'select * from tab_info order by sort'
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        datas = list()
        for info in results:
            tab = TabInfo()
            tab.name = info[0]
            tab.icons_selected = info[1]
            tab.icons_unselected = info[2]
            tab.sort = info[3]
            tab.id = info[4]

            sql = 'select * from tab_child_info where tab_id = %s order by sort' % tab.id
            cursor.execute(sql)
            child_results = cursor.fetchall()
            child_datas = list()
            for child_info in child_results:
                child_tab = TabChildInfo()
                child_tab.tab_id = child_info[1]
                child_tab.tab_name = child_info[2]
                child_tab.source = child_info[3]
                child_tab.platform = child_info[4]
                child_tab.sort = child_info[5]
                child_tab.show_type = child_info[6]
                child_tab.show = child_info[7]
                child_datas.append(child_tab.__dict__)

            tab.tab_child_infos = child_datas
            datas.append(tab.__dict__)

        cursor.close()
        db.close()
        return datas

    @staticmethod
    def get_home_info():
        sql = 'select * from home_title order by sort'
        db = db_base.DbBase.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()

        datas = list()
        for info in results:
            tab = HomeTitle()
            tab.style = info[0]
            tab.tile = info[1]
            tab.image_url = info[2]
            tab.click_url = info[3]
            tab.sort = info[4]
            tab.id = info[5]

            sql = 'select * from home_content where title_id = %s order by sort' % tab.id
            cursor.execute(sql)
            child_results = cursor.fetchall()
            child_datas = list()
            for child_info in child_results:
                child_tab = HomeContent()
                child_tab.content = child_info[0]
                child_tab.image_url = child_info[1]
                child_tab.click_url = child_info[2]
                child_tab.sort = child_info[3]
                child_tab.description = child_info[4]
                child_tab.id = child_info[5]
                child_tab.title_id = child_info[6]
                child_datas.append(child_tab.__dict__)

            tab.home_contents = child_datas
            datas.append(tab.__dict__)

        cursor.close()
        db.close()
        return datas

    @staticmethod
    def get_cll_info(source, platform, page):
        count = 20
        p = int(page)
        # sql = 'select * from cll where source = %s and platform = %s order by send_time desc limit %d offset %d' % \
        #       (source, platform, count, (p-1)*20)
        sql = "select * from cll "
        if source is not None and source != '""':
            s = 'where source = %s ' % source
            sql += s
        if platform is not None and platform != '""':
            if sql.find('where') != -1:
                pl = f'and platform = %s ' % platform
            else:
                pl = f'where platform = %s ' % platform
            sql += pl
        o = 'order by send_time desc limit %d offset %d' % (count, (p-1)*20)
        sql += o

        db = db_base.DbBase.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        datas = []
        for info in results:
            cll_info = CllInfo()
            cll_info.id = info[0]
            cll_info.title = info[1]
            cll_info.sub_title = info[2]
            cll_info.url = info[3]
            cll_info.image = info[4]
            cll_info.image_urls = info[5]
            cll_info.description = info[6]
            cll_info.source = info[7]
            cll_info.platform = info[8]
            cll_info.level = info[9]
            cll_info.top = info[10]
            cll_info.type = info[11]
            cll_info.send_time = info[12]
            datas.append(cll_info.__dict__)
        cursor.close()
        db.close()
        return datas
