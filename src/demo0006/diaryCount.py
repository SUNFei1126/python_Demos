# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/19.
 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词
'''

import os,re

path = 'diaries'
files = os.listdir(path)

def get_key_word(words):
    dict = {}
    max = 0
    marked_key = ''
    for word in words:
        word = word.lower()
        if word in dict:
            dict[word] +=1
        else:
            dict[word] = 1
    for key,value in dict.items():
        if dict[key] >max:
            max = dict[key]
            marked_key = key
    print(marked_key,max)

for f in files:
    with open(os.path.join(path,f)) as diary:
        words = re.findall("[a-zA-Z]+'*-*[a-zA-Z]*", diary.read())
        get_key_word(words)