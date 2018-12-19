# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/19.
  你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
'''
import os
from PIL import Image

path = 'pic'

for f in os.listdir(path):
    img = Image.open(os.path.join(path,f))
    width = img.size[0]
    height = img.size[1]
    out = img
    if width > 1136:
        width = 1136
        out = img.resize((width,height),Image.ANTIALIAS)
    if height > 640:
        height = 640
        out = img.resize((width,height),Image.ANTIALIAS)
    out.save('pic/result/'+f)