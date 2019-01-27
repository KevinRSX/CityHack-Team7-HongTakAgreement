import re
from bs4 import BeautifulSoup
from sys import argv
from . import entity_name
import json

def extract(soup):
    """
    @param: the soup of the xml file

    @return:
        {
            'entity_name': {
                value: ,
                page: ,               # counted from zero
                position: (x0, y0, x1, y1)
            }
        }
    """
    res = { }
    pages = soup.find_all('page')
    # print(pages)
    res['entity_name'] = entity_name.from_pages(pages)
    return res


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        soup = BeautifulSoup(f, 'xml')
    print('File opened')
    res = extract(soup)
    print(res)
