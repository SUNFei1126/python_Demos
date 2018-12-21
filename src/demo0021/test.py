# coding=utf-8

#!/usr/bin/python3

'''
 Created by sunyufei on 2018/12/21.
'''
'''
通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
'''
import uuid
import hashlib
def encrypt_password(password):
    salt = uuid.uuid4().hex
    result = password
    for i in range(10):
        result = hashlib.sha256(salt.encode() + result.encode()).hexdigest()
    return salt + ':' + result


if __name__ =='__main__':
    pw = 'abcd123456'
    print("The password stored in the database is:" + encrypt_password(pw))