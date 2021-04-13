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
from business_yimaitong import blood_latest

from apscheduler.schedulers.blocking import BlockingScheduler
import time


class Main:

    @staticmethod
    def zongliuzixun():
        # 肿瘤资讯
        # 最新
        top = TopLatest()
        DbOperator.insert(top.get_all_data())
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
        DbOperator.insert(ppn.get_data_plugin())
        # 免费医疗
        ct = ClinicalTrials()
        DbOperator.insert(ct.get_data_plugin())
        # 淋巴瘤快讯
        lbll = LinBaLiuLatest()
        DbOperator.insert(lbll.get_data_plugin())

    @staticmethod
    def yiyingxinsheng():
        # 亿迎新生
        # 疾病百科
        de = DiseaseEncy()
        s_datas = list()
        for i in range(3):
            s_datas.extend(de.get_html(i + 1))
        DbOperator.insert(s_datas)
        # 大咖讲堂
        expert = ExpertClass()
        DbOperator.insert(expert.get_html())
        # 科普专栏
        science = PopularScience()
        DbOperator.insert(science.get_html())

    @staticmethod
    def yimaitong():
        # 醫脈通
        blood = blood_latest.Blood()
        bloods = []
        for i in range(2):
            bloods.extend(blood.get_data_plugin(i * 10))
        DbOperator.insert(bloods)

    # 从数据库中通过api将数据插入到bmob中
    # @staticmethod
    # def database_bmob(start, end):
    #     ope = OperateData()
    #     ope.insert(ope.get_datas(start, end))
        # ope.update(ope.get_datas(1, end))

    @staticmethod
    def execute():
        start = DbOperator.query_size()
        print(str(start))
        # releaseTime
        Main.zongliuzixun()
        # insert
        # Main.yangshenmiao()
        # sendtime
        Main.linbaliuzhijia()
        # 无
        Main.yiyingxinsheng()
        Main.yimaitong()
        end = DbOperator.query_size()
        print(str(start) + '===' + str(end))

        print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


if __name__ == '__main__':
    Main.execute()
    # Main.database_bmob(412, 557)

    # 定时服务 每天每小时执行一次
    # schedule = BlockingScheduler()

    # 1.coalesce：当由于某种原因导致某个job积攒了好几次没有实际运行（比如说系统挂了5分钟后恢复，有一个任务是每分钟跑一次的，
    # 按道理说这5分钟内本来是“计划”运行5次的，但实际没有执行），如果coalesce为True，下次这个job被submit给executor时，只会执行1次，
    # 也就是最后这次，如果为False，那么会执行5次（不一定，因为还有其他条件，看后面misfire_grace_time的解释）
    # 2.max_instance: 就是说同一个job同一时间最多有几个实例再跑，比如一个耗时10分钟的job，被指定每分钟运行1次，
    # 如果我们max_instance值为5，那么在第6~10分钟上，新的运行实例不会被执行，因为已经有5个实例在跑了
    # 3.misfire_grace_time：设想和上述coalesce类似的场景，如果一个job本来14:00有一次执行，但是由于某种原因没有被调度上，
    # 现在14:01了，这个14:00的运行实例被提交时，会检查它预订运行的时间和当下时间的差值（这里是1分钟），大于我们设置的30秒限制，
    # 那么这个运行实例不会被执行。

    # 每天16-18点的0-4分钟执行 执行频率是5秒钟
    # schedule.add_job(func=Main.execute, coalesce=True, max_instances=3, misfire_grace_time=300, trigger='cron',
    #                 hour='12, 19', minute='30')
    # 每五秒执行一次
    # schedule.start()
