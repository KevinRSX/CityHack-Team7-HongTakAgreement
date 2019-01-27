"""
usage:
    ./test_t_res pdf json page
"""

from PIL import Image, ImageDraw
from sys import argv
import json

PAPAR_SIZE = (1654, 2339)

def remap(p0, p1, paper_size, image_size):
    p0_x = p0[0] * image_size[0] / paper_size[0]
    p0_y = p0[1] * image_size[1] / paper_size[1]
    p1_x = p1[0] * image_size[0] / paper_size[0]
    p1_y = p1[1] * image_size[1] / paper_size[1]
    return (p0_x, p0_y, p1_x, p1_y)

pdf_name = argv[1]
json_name = argv[2]
page_num = int(argv[3])

im = Image.open(pdf_name)

with open(json_name, 'r') as f:
    jj = json.load(f)

max_x = 0;
max_y = 0
min_x = 9999999
min_y = 99999999
## GEt the largest indx
for page in jj['pages']:
    for rect in page['tags']:
        min_x = min(rect['pt0'][0], min_x)
        min_x = min(rect['pt1'][0], min_x)
        min_y = min(rect['pt0'][1], min_y)
        min_y = min(rect['pt1'][1], min_y)
        max_x = max(rect['pt0'][0], max_x)
        max_x = max(rect['pt1'][0], max_x)
        max_y = max(rect['pt0'][1], max_y)
        max_y = max(rect['pt1'][1], max_y)

print('min x:', min_x, 'min y:', min_y)
print('max x:', max_x, 'max y:', max_y)


for i in jj['pages']:
    if i['pageId'] == page_num:
        page = i

image_size = im.size
draw = ImageDraw.Draw(im)

for rect in page['tags']:
    point0 = rect['pt0']
    point1 = rect['pt1']
    if 'entityType' in rect:
        rect_name = rect['entityType']
    else:
        rect_name = 'Not given'
    box = remap(point0, point1, PAPAR_SIZE, image_size)
    print(box)
    draw.rectangle(box, outline='blue')
    draw.text(box[0:2], rect_name, fill='blue')

im.show()

