# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/20.
'''
'''
一个HTML文件，找出里面的链接。
'''
import urllib.request
import re

def find_links(website):
    html_content = urllib.request.urlopen(website).read()
    r = re.compile('href="(https://.*?)"')
    html_content = str(html_content,'utf-8')
    result = r.findall(html_content)
    return result

if __name__ =='__main__':
    links_list = find_links('http://www.taobao.com/')
    for link in links_list:
        print(link)