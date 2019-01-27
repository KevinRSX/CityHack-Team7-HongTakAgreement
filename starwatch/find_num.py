import re
from bs4 import BeautifulSoup
from sys import argv
# ^\W*opinion\W*$
def calc_ave(soup):
    texts = soup.find_all('text')
    i=0
    cnt=0.0
    for text in texts:
        if 'size' in text.attrs:
            i+=1
            cnt+=float(text['size'])
    return cnt/i

def extract_first(soup):
    """
    @param: the soup of the xml file
    @return:
        {
            'auditor':
            value: '
            page: ,
            position: ,
        }
    """
    ave = calc_ave(soup)
    res = {}
    i = 0
    p = 0
    pages = soup.find_all('page')
    for pg in pages:
        messages = extract_from_page_by_line(pg,'net profit',ave,p)
        p+=1
        if messages is not None:
            for message in messages:
                res[i] = messages[message]
                i+=1
    return res

def extract_from_page_by_line(page,pattern,ave,num):
    """
    @param page: soup of the last page

    @return the name found or None if not found
    """
    lines = page.find_all('textline')
    adt_re = re.compile(pattern, flags=re.IGNORECASE)
    res = {}
    i = 0
    for line in lines:
        text = line.find("text")
        if 'size' in text.attrs and float(text['size'])>ave:
            message = line.find('content', string=adt_re)
            if message is not None:
                res[i] = [message,line['bbox'],num]
                i+=1
    return res

def extract(soup):
    contents = extract_first(soup)
    ops = {}
    i = 0
    for content in contents:
        n = int(contents[content][2])+1
        page = soup.find('page',id=n)
        opinions = extract_from_page_by_line(page,r'^\W*net profit\W*$',0,n-1)
        if opinions is not None:
            for opinion in opinions:
                opinions[opinion][0] = opinions[opinion][0].get_text()
                ops[i] = opinions[opinion]
                i+=1
        answer_box = None
        i = 0
    return ops

if __name__ == '__main__':
    with open(argv[1], 'r') as f:
        soup = BeautifulSoup(f, 'xml')
        print('File opened')
        ops = extract(soup)
        for opinion in ops:
            print(ops[opinion])
