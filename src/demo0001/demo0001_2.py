# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/7.
'''
#第 demo0001 题：**做为 Apple Store App 独立开发者，
# 你要搞限时促销，为你的应用**生成激活码**（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）
import random, string

# forSelect = string.ascii_letters + "0123456789"
forSelect = string.ascii_letters + string.digits

def generate(count, length):
    # count = 200
    # length = 20

    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        print(Re)
        yield Re

if __name__ == "__main__":
    s=generate(200, 20)
    for a in s:
        print(a)