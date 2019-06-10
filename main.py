from business_zhongliuzixun.top_hot import TopHot
from business_zhongliuzixun.top_latest import TopLatest
from business_linbaliu.professional_point_new import ProfessionalPointNew
from business_linbaliu.clinical_trials import ClinicalTrials
from business_linbaliu.linbaliu_latest import LinBaLiuLatest
from business_yiyingxinsheng.disease_encyclopedia import DiseaseEncy
from business_yiyingxinsheng.expert_class import ExpertClass
from business_yiyingxinsheng.popular_science import PopularScience
from business_gongzhonghao.spider_gzh import SpiderGZH
from db.db_operate import DbOperator
from bmob.operate_data import OperateData


class Main:

    @staticmethod
    def zongliuzixun():
        # 肿瘤资讯
        # 最新
        top = TopLatest()
        DbOperator.insert(top.loop_data(30))
        # 最热
        hot = TopHot()
        DbOperator.insert(hot.get_data_plugin(0, 1000))

    @staticmethod
    def yangshenmiao():
        # 杨申淼的公众号
        name = '杨申淼'
        index = 0
        spider = SpiderGZH(name, index)
        DbOperator.insert(spider.handle_datas(spider.get_all_article()))

    @staticmethod
    def linbaliuzhijia():
        # 淋巴瘤
        # 专家说
        ppn = ProfessionalPointNew()
        DbOperator.insert(ppn.get_data_plugin(0, 100))
        # 免费医疗
        ct = ClinicalTrials()
        DbOperator.insert(ct.get_data_plugin(0, 10))
        # 淋巴瘤快讯
        lbll = LinBaLiuLatest()
        DbOperator.insert(lbll.get_data_plugin(0, 10))

    @staticmethod
    def yiyingxinsheng():
        # 亿迎新生
        # 疾病百科
        de = DiseaseEncy()
        s_datas = list()
        for i in range(2):
            s_datas.extend(de.get_html(i + 1))
        DbOperator.insert(s_datas)
        # 大咖讲堂
        expert = ExpertClass()
        DbOperator.insert(expert.get_html())
        # 科普专栏
        science = PopularScience()
        DbOperator.insert(science.get_html())

    # 从数据库中通过api将数据插入到bmob中
    @staticmethod
    def database_bmob(start, end):
        ope = OperateData()
        ope.insert(ope.get_datas(start, end))

    @staticmethod
    def execute():
        start = DbOperator.query_size()
        print(str(start))
        Main.zongliuzixun()
        Main.yangshenmiao()
        Main.linbaliuzhijia()
        Main.yiyingxinsheng()
        end = DbOperator.query_size()
        print(str(start) + '===' + str(end))
        Main.database_bmob(start, end)


if __name__ == '__main__':
    # Main.execute()
    Main.database_bmob(193, 242)
