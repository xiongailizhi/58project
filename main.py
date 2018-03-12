from multiprocess import Pool
from channel_extract import channel_lists
from page_parsing import getUrlList
from page_parsing import get_item_info

def getAllUrlLists(channel):
    for num in range(1,101):
        for url in getUrlList(channel,num):
            get_item_info(url)

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(getAllUrlLists,channel_lists.split())