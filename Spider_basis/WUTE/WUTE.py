from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    url = 'http://sie.whut.edu.cn/xsgz/xzfc/'
    page_text = requests.get(url=url,headers = header).content.decode('utf-8')


    soup = BeautifulSoup(page_text,'lxml')

    li_list = soup.select('.art_list > ul > li > span')
    fp = open('./wute.txt','w',encoding='utf-8')
    print(li_list)
    for n in li_list:
        title = n.a.string
        detail_url = 'http://sie.whut.edu.cn/xsgz/xzfc/'+n.a['href']
        detail_page_text = requests.get(url=detail_url,headers=header).content.decode('utf-8')

        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='art_text')

        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'successfully')




