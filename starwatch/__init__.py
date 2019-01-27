import extractor
from bs4 import BeautifulSoup

def extract(file_name):
    with open(file_name) as f:
        soup = BeautifulSoup(f, 'xml')
    extractor.extract(soup)
