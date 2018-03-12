from bs4 import BeautifulSoup
import requests
import time
import pymongo
from __init__ import reget

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list3']
item_info = ceshi['item_info4']

#获取每个页面的每个商品的地址
def getUrlList(channel,page,whosells=1):
    '''http://bj.58.com/tiaozao/pn2/'''
    channel_url = '{}{}/pn{}/?islocal=1'.format(channel,str(whosells),str(page))
    wb_data = reget(channel_url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('div.left > a.title.t')
    for link in links:
        url = link.get('href').split('?')[0]
        #只选择符合条件的url
        if 'bj.58.com' in url:
            item_link = url
            url_list.insert_one({'url':item_link})
            # get_item_info(item_link)
            print(item_link)
        else:
            pass


def get_item_info(url):
    wb_data = reget(url)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # no_longer_exist = '404' in soup.find('script',type = "text/javascript").get('src').split('/')#判断是否404
    # if no_longer_exist:
    #     pass
    try:
        try:
            title = soup.title.text.replace("\r", "").replace("\n", "").replace(" ", "")
        except:
            title = None
        try:
            price = soup.select('span.price.c_f50')[0].text.replace("\t","")
        except:
            price = None
        try:
            date = soup.select('li.time')[0].text
        except:
            date = None
        # 如果没有则显示None
        if soup.find_all('span', 'c_25d'):
            try:
                area = list(soup.select('.c_25d a')[0].stripped_strings)
            except:
                area = "不明"
        else:
            area = "不明"
        item_info.insert_one({'url':url,'title':title,'price':price,'date':date,'area':area})
        print({'url':url,'title':title,'price':price,'date':date,'area':area})
    except:
        print('error')

# get_item_info('http://bj.58.com/zixingche/32526510092999x.shtml')
