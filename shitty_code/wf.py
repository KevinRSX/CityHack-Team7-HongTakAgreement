from sys import argv
import re
import csv

def add_freq(d, w):
    w = w.lower()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

def add_freqs(d, line):
    """
    Add frenquencies into d

    @return: the number of words added
    """
    words = re.split(r'\W+', line)
    if len(words) > 0 and words[0] == '':
        words.pop(0)
    if len(words) > 0 and words[-1] == '':
        words.pop()
    for wd in words:
        add_freq(d, wd)
    return len(words)

def wf_in_soup(soup):
    """
    calculate the word frequency in a soup
    """
    tmp = {}
    contents = soup.find_all('content')
    for content in contents:
        add_freqs(tmp, content.get_text())
    return tmp

def wf_in_soups(soups):
    """
    calculate the word frequency insoups
    """
    tmp = {}
    for soup in soups:
        contents = soup.find_all('content')
        for content in contents:
            add_freqs(tmp, content.get_text())
    return tmp

def read_word_frequence(f, max_lines=500):
    reader = csv.reader(f)
    count = 0
    res = {}
    for row in reader:
        if count >= max_lines:
            break
        res[row[0]] = float(res[row[1]])
        count += 1

    return res


if __name__ == '__main__':
    filenames = argv[1:]

    freqs = {}
    count = 0
    for filename in filenames:
        with open(filename, 'r') as f:
            for row in f:
                count += add_freqs(freqs, row)

    res = [(k, freqs[k]/count) for k in freqs]
    res.sort(key=lambda x: -x[1])
    print('Total:', count)
    for item in res:
        print(item[0], ', ', item[1], sep='')
