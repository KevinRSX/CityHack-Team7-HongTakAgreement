from sys import argv
import re
from bs4 import BeautifulSoup

def add_freq(d, w):
    w = w.lower()
    if w in d:
        d[w] += 1
    else:
        d[w] = 1

def add_freq_for_line(d, line):
    words = re.split(r'\W+', line)
    for wd in words:
        add_freq(d, wd)

def add_freq_for_page(d, page):
    index = int(page['id'])-1
    lines = page.find_all('textline')
    d[index] = {}
    for line in lines:
        add_freq_for_line(d[index],line.get_text())

filename = argv[1]
freqs = {}
with open(filename, 'r') as f:
    soup = BeautifulSoup(f,'xml')
    print('File Opened')
    pages = soup.find_all('page')
    for page in pages:
        add_freq_for_page(freqs,page)

# res = [(k, freqs[k]) for k in freqs]
# res.sort(key=lambda x: -x[1])
for pgf in freqs:
    print(freqs[pgf])
