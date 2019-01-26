from sys import argv
import re

def add_freq(d, w):
    w = w.lower()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

def add_freqs(d, line):
    words = re.split(r'\W+', line)
    if len(words) > 0 and words[0] == '':
        words.pop([0])
    if len(words) > 0 and words[-1] == '':
        words.pop()
    for wd in words:
        add_freq(d, wd)

def wf_in_soup(soup):
    """
    calculate the word frequency in a soup
    """
    tmp = {}
    contents = soup.find_all('content')
    for content in contents:
        add_freqs(tmp, content.get_text())
    return tmp


if __name__ == '__main__':
    filename = argv[1]

    freqs = {}
    with open(filename, 'r') as f:
        for row in f:
            add_freqs(freqs, row)

    res = [(k, freqs[k]) for k in freqs]
    res.sort(key=lambda x: -x[1])
    for i in range(500):
        print(res[i])
