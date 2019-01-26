"""
Usage:
    ./to_txt floder
"""

import re
import sys
from sys import argv
from pathlib import Path

pathname = argv[1]
p = Path(pathname)
names = [x for x in p if str(x)[-3:] == '.py']



