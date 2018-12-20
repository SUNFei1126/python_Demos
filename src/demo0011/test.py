# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/20.
'''

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
北京
程序员
公务员
领导
牛比
牛逼
你娘
你妈
love
sex
jiangge
"""

def filter_words(words):
    file_object = open('filtered_words.txt','rb')
    filtered_words = []
    for line in file_object:
        line = str(line,'utf-8')
        filtered_words.append(line.strip('\n').strip('\r'))
    file_object.close()

    filtered = False
    for filtered_word in filtered_words:
        if filtered_word in words:
            filtered = True
            break

    if filtered is True:
        print('Freedom')
    else:
        print('Human Rights')

if __name__ == '__main__':
    while True:
        input_words = input('Input some words:')
        filter_words(input_words)