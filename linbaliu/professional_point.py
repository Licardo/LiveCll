from bs4 import BeautifulSoup
from base.net_get import NetGet


class ProfessionalPoint(NetGet):
    def get_html(self):
        url = 'https://mp.weixin.qq.com/s/mGZYpTfhLNaC1HSux23nvQ'
        header = {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 '
                                '(KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
                  'Proxy-Connection': 'keep-alive'}
        get = NetGet()
        str_json = get.get(url, header=header)
        # 解析str中的数据 交给BeautifulSoup处理
        soup = BeautifulSoup(str_json, 'html.parser')
        div_content = soup.find('div', id='js_content')
        section = div_content.find('section', style='box-sizing: border-box;')
        items = section.find_all('a')
        for item in items:
            href = item['href']
            print(href)
            print(item.find('span').get_text())
        print(len(items))


if __name__ == '__main__':
    point = ProfessionalPoint()
    point.get_html()
