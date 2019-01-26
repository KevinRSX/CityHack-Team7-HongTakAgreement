import re
import json

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


with open("Training/1/1_tagged.json") as fobj:
    tags = json.load(fobj)

with open("1_tagged_formatted.json", "w") as fobj:
    json.dump(tags, fobj, indent=4)
