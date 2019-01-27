import re
from sys import argv

"""
Usage
    ./combine_test_tag infile outfile
"""

in_filename = argv[1]
out_filename = argv[2]

with open(in_filename, 'r') as f:
    sori = f.read()

ss1 = re.sub(r'</text>\W*<text .*?>', '', sori)
ss2 = re.sub(r'<text.*?>', '', ss1)
ss3 = re.sub(r'</text>', '', ss2)

with open(out_filename, 'w') as f:
    f.write(ss3)

