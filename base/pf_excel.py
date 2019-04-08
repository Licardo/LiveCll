
import pandas as pd

# 所有与excel相关的操作都可以抽象到这里


class Excel(object):

    @staticmethod
    def write_excel(datas, name):
        df = pd.DataFrame(data=datas)
        write = pd.ExcelWriter('latest.xls')
        df.to_excel(write, sheet_name=name, index=None)
        write.save()
        write.close()
        print(df)

    @staticmethod
    def read_excel():
        print('read byte from excel')
