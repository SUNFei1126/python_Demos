# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/6.
'''
from PIL import Image, ImageDraw, ImageFont

img = Image.open('mywechat.jpg')
draw = ImageDraw.Draw(img)
myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=80)
fillcolor = "#ff0000"
width, height = img.size
draw.text((40,40),'hello', font=myfont, fill=fillcolor)
img.save('result.jpg','jpeg')