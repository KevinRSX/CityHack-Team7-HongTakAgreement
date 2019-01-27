import re
from bs4 import BeautifulSoup
from sys import argv
import json

def extract(soup):
    """
    @param: the soup of the xml file

    @return:
        {
            'total income':
            'net profit':
            'total equity':
        }
    """
    res = {}
    # print(pages)
    return res

def extract_from_page_by_line(page, pattern, num):
    """
    @param page: soup of the last page

    @return the name found or none if not found
    """
    lines = page.find_all('textline')
    adt_re = re.compile(pattern, flag = re.IGNORECASE)

    res = {}
    i = 0
    for line in lines:
        text = line.find("text")
        message = line.find('content', string=adt_re)
        if message is not None:
            res[i] = [message, line['bbox'], num]
            i += 1
    return res
