# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/20.
'''
"""
第 0013 题： 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)
"""

import urllib.request
import re
import os

def fetch_pic(url):
    html_content = urllib.request.urlopen(url).read()
    r = re.compile('<img pic_type="0" class="BDE_Image" src="(.*?)"')
    picture_url_list = r.findall(html_content.decode('utf-8'))

    os.mkdir('pictures')
    os.chdir(os.path.join(os.getcwd(), 'pictures'))
    for i in range(len(picture_url_list)):
        picture_name = str(i) + '.jpg'
        try:
            urllib.request.urlretrieve(picture_url_list[i], picture_name)
            print("Success to download " + picture_url_list[i])
        except:
            print("Fail to download " + picture_url_list[i])


if __name__ == '__main__':
    fetch_pic("http://tieba.baidu.com/p/2166231880")