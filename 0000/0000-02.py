# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/6.
'''
from PIL import Image, ImageDraw, ImageFont
import sys, os, random

num = str(random.randint(1,99))
def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('Arial.ttf', size=40)
    fillcolor =  "#ff0000"
    width, height = img.size
    draw.text((width-40, 0), num, font=myfont, fill=fillcolor)
    # draw.text((width-40, 0), "3", (256, 0, 0), font=fillcolor)
    img.save('0000-02-result-mywechat.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    image = Image.open('mywechat.jpg')
    add_num(image)