from .extractor import extract as ex
from .find_auditor import extract as exp
from bs4 import BeautifulSoup
from . import toxml

def extract_entity(file_name):
    with open(file_name) as f:
        soup = BeautifulSoup(f, 'xml')
    return ex(soup)

def extract_auditor(file_name):
    with open(file_name) as f:
        soup = BeautifulSoup(f, 'xml')
    return exp(soup)
