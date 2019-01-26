import re

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

for i in range(0, 108):
    with open("../CityU-Hackathon-2019/Testing/67/hocr/67-" + str(i) + ".hocr", "r") as fobj:
        html = cleanhtml(fobj.read())
        with open("67-" + str(i) + ".txt", "w") as output:
            output.write(html)
