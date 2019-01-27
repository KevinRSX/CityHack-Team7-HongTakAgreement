import os
from sys import argv
from pathlib import Path


def toxml(out_file, in_file):
    os.system('pdf2txt.py ' +  ' -o converted.xml ' + in_file)
    os.system('python3 starwatch/combine_text_tag_to_content_tag.py ' + 'converted.xml ' + out_file)
    os.remove('converted.xml')
