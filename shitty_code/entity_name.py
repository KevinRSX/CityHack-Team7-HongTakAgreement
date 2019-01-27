import re
import wf

MAX_FREQUENT_WORDS = 300
MAX_TESTED_FREQUENT_WORDS = 100
MAX_FRONT_PAGES_NUMBER = 3

with open('./postal_address_words.txt', 'r') as f:
    _address_word_list = [r for r in f]

with open('./word_frequencies.txt', 'r') as f:
    _word_requency_list = wf.read_word_frequence(f, MAX_FREQUENT_WORDS)

def from_pages(pages):
    """
    @param: pages in the document soup
    """
    res = from_last_page(pages[-1])
    if res is None:
        pass
    if res is not None:
        parent = res.parent
        bbox = parent['bbox']
        position = tuple(bbox.split(','))
        accendant = parent
        while accendant.name != 'page':
            accendant = accendant.parent
        page = int(accendant['id']) - 1
        return {
                'value': res.get_text(),
                'page': page,
                'position': position}

def from_last_page(page):
    """
    @param page: soup of the last page

    @return the <content> holding the name found or None if not found
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

def from_front_pages(pages, page_limits=3):
    """
    @param page: soups of the pages

    @return the <content> holding the name found or None if not found
    """
    upper_bound = min(len(pages), page_limits)
    word_frequencies = wf.wf_in_soups(pages[:upper_bound])
    word_frequencies_l = [(k, word_frequencies[k]) for k in word_frequencies]
    word_frequencies_l.sort(key=lambda x : - x[1])
    upper_bound = min(len(word_frequencies_l), MAX_TESTED_FREQUENT_WORDS)
    selected_word_frequencies = word_frequencies_l[:upper_bound]
    special_words = [wf[0] for word in selected_word_frequencies \
            if word not in _word_requency_list]
    pass






