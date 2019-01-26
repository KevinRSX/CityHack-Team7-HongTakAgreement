import re
from bs4 import BeautifulSoup
from sys import argv

def extract(soup):
    """
    @param: the soup of the xml file

    @return:
        {
            'entity_name':
        }
    """
    res = { }
    pages = soup.find_all('page')
    # print(pages)
    res['entity_name'] = extract_entity_name_from_last_page(pages[-1]).get_text()
    return res


if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        soup = BeautifulSoup(f, 'xml')
    print('File opened')
    res = extract(soup)
    print(res)
