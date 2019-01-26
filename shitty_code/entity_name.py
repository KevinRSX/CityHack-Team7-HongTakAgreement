import re

with open('./postal_address_words.txt', 'r') as f:
    _address_word_list = [r for r in f]

def from_soup(pages):
    """
    @param: pages in the document soup
    """
    pass

def from_last_page(page):
    """
    @param page: soup of the last page

    @return the name found or None if not found
    """

    lmt_re = re.compile('Ltd|limited|corporation|' + \
            'corperated|corp|inc|incoperation',
            flags=re.IGNORECASE)
    res = page.find('content', string=lmt_re)
    if res is not None:
        return res
    contents = page.find_all('content')
    last = None
    for content in contents:
        if last is not None and is_address(content):
            res = last
    if res is not None:
        return res
    return res

def is_address(s):
    """
    determine whether s is an address
    """
    for word in _address_word_list:
        if word in s:
            return True
    return False



