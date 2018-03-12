from multiprocess import Pool
import pymongo
from page_parsing import get_item_info

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
urls = ceshi['url_list3']

links = []
for url in urls.find():
    links.append(url['url'])
# print(links)

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(get_item_info,links)