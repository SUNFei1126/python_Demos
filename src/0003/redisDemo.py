# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/19.
 将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中
'''

import redis ,uuid
import random, string

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
    # s = generate(200, 20)
    r = redis.StrictRedis(host='localhost', port=6379,password='123456')
    # i = 0
    # for a in s:
    #     r.set('key_id' + str(i), a)
    #     i=i+1
    for i in range(200):
        print(str(r.get("key_id" + str(i)),'utf-8'))
