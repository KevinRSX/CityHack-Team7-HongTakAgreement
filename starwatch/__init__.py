from .find_entity import extract as ex
from .find_auditor import extract as exp
from .find_num import extract as expe
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

def extract_num(file_name):
    with open(file_name) as f:
        soup = BeautifulSoup(f, 'xml')
    return expe(soup)
