import re
def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

words = ''
with open("output.xml") as fobj:
    words = fobj.read()
    cleanhtml(words)

wordfreq = []
wordlist = words.split()

for w in wordlist:
    wordfreq.append(wordlist.count(w))

with open("freq.txt", "w") as fobj:
    fobj.write(zip(wordlist, wordfreq))
