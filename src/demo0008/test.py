# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/20.
'''
"""
第 0008 题：一个HTML文件，找出里面的正文。
"""
import urllib.request
import re

def get_body(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<p>(?:<.[^>]*>)?(.*?)(?:<.[^>]*>)?</p>')
    html_content = str(html_content.decode('GBK').encode('UTF-8'),'utf-8')
    # print(html_content)
    result = r.findall(html_content)
    return result

if __name__ == '__main__':
    body = get_body('http://tech.163.com/14/1219/01/ADPT7MTE000915BF.html')
    for l in body:
        print(l)