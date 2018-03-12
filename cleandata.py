from multiprocess import Pool
import pymongo
from page_parsing import get_item_info

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
urls = ceshi['url_list3']
prices = ceshi['item_info3']

for i in prices.find():
    price = str(i['price']).replace(' ','').replace('\r','').replace('\n','').replace('\u0009','').replace('\t','')
    prices.update({'_id':i['_id']},{'$set':{'price':price}})