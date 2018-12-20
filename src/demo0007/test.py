# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/20.
'''
"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import os
import sys


def code_lines(target_file):
    # Declare returned values
    total_lines = 0
    empty_lines = 0
    comment_lines = 0

    file_object = open(target_file, 'rb')
    for line in file_object:
        # Split the string
        word_list = line.split()
        if word_list == []:
            empty_lines += 1
        elif str(word_list[0],'utf-8').startswith('#'):
            comment_lines += 1
        total_lines += 1

    file_object.close()
    return total_lines, empty_lines, comment_lines


if __name__ == "__main__":
    dir_path='E:\python_oneday_oneproblem\python1D1P\src\demo0001'
    t_lines = 0
    e_lines = 0
    c_lines = 0
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path):
            t, e, c = code_lines(file_path)
            t_lines += t
            e_lines += e
            c_lines += c
    print("Total lines: %s. Empty lines: %s. Comment Lines: %s." % (t_lines, e_lines, c_lines))