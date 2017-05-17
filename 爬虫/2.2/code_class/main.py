from multiprocessing import Pool
from code_class import channel_list
from page_parsing import get_links_from

def get_all_links(channel):
    for num in range(1,101):
        get_links_from(channel,num)

if __name__ == '__main__':
    pool=Pool()
    pool.map(get_all_links,channel_list.split())