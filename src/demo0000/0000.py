# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/6.
 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
'''
from  PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys, os, random

num = str(random.randint(1,99))
imagePath =os.path.join(sys.path[0], 'mywechat.jpg')
savePath=os.path.join(sys.path[0], 'demo0000-01-result-mywechat_number.jpg')

def add_num(im, wDraw, hDraw):
    font =  ImageFont.truetype('arial.ttf', 30)
    draw =  ImageDraw.Draw(im)
    draw.ellipse(
        (radioX, radioY, radioX + 30, radioY + 30), fill ='red', outline='red')
    im.show()
    draw.text((wDraw, hDraw), num, font=font, fill='white')
    im.save(savePath, 'jpeg')

if __name__ == '__main__':
    im =  Image.open(imagePath)
    w, h = im.size
    print('Original image size:  %sx%s' %(w,h))
    wDraw = int(0.9 * w)
    hDraw = int(0.01 * h)
    radioX = wDraw
    radioY = hDraw
    print('radioX:', radioX)
    print('radioY:', radioY)
    add_num(im, wDraw, hDraw)