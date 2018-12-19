# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/19.
 任一个英文的纯文本文件，统计其中的单词出现的个数。
'''
#统计的是文本的所有的单词个数

import io,re

count = 0

with io.open('test.txt','r') as file:
    for line in file.readlines():
        list = re.findall("[a-zA-Z]+'*_*[a-zA-Z]*",line)
        print(list)
        count +=len(list)
print(count)