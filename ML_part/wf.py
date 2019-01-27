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
    for wd in words:
        add_freq(d, wd)

filename = argv[1]

freqs = {}
with open(filename, 'r') as f:
    for row in f:
        add_freqs(freqs, row)

res = [(k, freqs[k]) for k in freqs]
res.sort(key=lambda x: -x[1])
for i in range(500):
    if len(res[i][0])>4:
        print(res[i])
