import os,Image
from pytesser import *
from PIL import *

os.chdir('C:\\')
im=Image.open('a.jpg')
print im.size[0]
print im.size[1]
box=im.copy()
box=(3,2,47,23)
region=im.crop(box)

imgry=region.convert('L')
threshold=138
table=[]
for i in range(256):
    if i<threshold:
        table.append(0)
    else:
        table.append(1)
out=imgry.point(table,'1')
print image_to_string(out)
out.save('1.jpg','JPEG')




"""
os.chdir('C:\\')
im=Image.open('222.jpg')
print image_to_string(im)
"""


