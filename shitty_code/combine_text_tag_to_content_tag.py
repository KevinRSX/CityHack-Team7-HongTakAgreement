import re
import bs4.element
from bs4 import BeautifulSoup
from sys import argv

in_filename = argv[1]
out_filename = argv[2]

with open(in_filename, 'r') as f:
    soup = BeautifulSoup(f, 'xml')

textlines = soup.find_all('textline')
for textline in textlines:
    content = ''.join(
            [x.string for x in textline \
                    if x is not None and type(x) is bs4.element.Tag
                    and x.string is not None])
    content_tag_cont = '<content>{}</content>'.format(content)
    content_soup = BeautifulSoup(content_tag_cont, 'xml')
    textline.append(content_soup)

with open(out_filename, 'w') as f:
    f.write(str(soup))


