# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/7.
 将 demo0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
'''
import random, string
import pymysql

# forSelect = string.ascii_letters + "0123456789"
forSelect = string.ascii_letters + string.digits

def generate(count, length):
    # count = 200
    # length = 20

    for x in range(count):
        Re = ""
        for y in range(length):
            Re += random.choice(forSelect)
        # print(Re)
        yield Re

def conmysql(codes):
    try:
        conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='test')
        cur = conn.cursor()
    except BaseException as e:
        print(e)
    else:
        try:
            cur.execute('CREATE DATABASE IF NOT EXISTS activation_code')
            cur.execute('USE activation_code')
            cur.execute('''CREATE TABLE IF NOT EXISTS code(
                                    id INT NOT NULL AUTO_INCREMENT,
                                    code VARCHAR(32) NOT NULL,
                                    PRIMARY KEY(id)
                                )''')
            for code in codes:
                cur.execute('INSERT INTO code(code) VALUES(%s)', (code))
                cur.connection.commit()
        except BaseException as e:
            print(e)
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    codes = generate(200,20)
    conmysql(codes)
    print("ok!")