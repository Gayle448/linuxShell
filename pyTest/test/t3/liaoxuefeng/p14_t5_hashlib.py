#!/usr/bin/python3
# -*- coding: utf-8 -*-
# --------------------------------------------------
# File Name: p14_t5_hashlib.py
# Author: hanxu
# AuthorSite: http://www.thesunboy.com/
# GitSource: https://github.com/hx940929/linuxShell
# Created Time: 2019-1-25-下午5:00
# ---------------------说明--------------------------
# hashlib,摘要算法简介.
# ---------------------------------------------------
# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
#
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。
# 它通过一个函数，把任意长度的数据转换为一个长度固定的数据串
# （通常用16进制的字符串表示）

import hashlib
import os
from _hashlib import HASH

# TODO 获取当前运行的py文件名,和调用了当前py文件的
# 上下文环境,比如当本py文件被调用时,能取到调用时的所在路径,调用的py文件名.
Hash_Type_Md5 = "md5"
Hash_Type_SHA1 = "sha1"


def getHash(type: str = Hash_Type_Md5) -> HASH:
    """
    获取hash校验对象.
    :param type:
    :return:
    """
    if type == Hash_Type_Md5:
        return hashlib.md5()
    elif type == Hash_Type_SHA1:
        return hashlib.sha1()


def md5CurrPy():
    """
    MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，
    通常用一个32位的16进制字符串表示
    :return:
    """
    curPyFile = os.getcwd() + "/p14_t5_hashlib.py"
    # print(__file__)当前执行文件名.
    md5obj = hashlib.md5()
    # print(type(md5obj)))
    # TODO 如何有更简单简洁方便的方法,来让编译器知道md5obj的类型.
    if isinstance(md5obj, HASH):
        with open(curPyFile, mode='r+') as curPyFileIO:
            if curPyFileIO and curPyFileIO.readable():
                # TODO 如何判断io.readline()方法是否读取到最后一行数据了?
                loop = True
                indexCount = 0
                while loop:
                    tmp = curPyFileIO.readline()
                    if tmp:
                        # print(tmp)
                        indexCount += 1
                        # 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的
                        md5obj.update(tmp.encode())
                    else:
                        loop = False
                md5value = md5obj.hexdigest()
                print("读取并计算文件md5结束.共计读取[%s]行,md5[%s]" % (indexCount, md5value))


def shaCurrpy():
    """
    SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。

比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长
    :return:
    """

    sha1obj = hashlib.sha1()
    with open(os.getcwd() + "/p14_t5_hashlib.py") as currpyobj:
        currpytext = currpyobj.read()
        sha1obj.update(currpytext.encode())
        print(sha1obj.hexdigest())


def py_salt():
    """
    使用py标准库来替代自己实现加盐策略的摘要算法
    :return:
    """
    import hmac
    message = b'Hello, world!'
    salt = b'secret'
    h = hmac.new(salt, message, digestmod='MD5')
    # 如果消息很长，可以多次调用h.update(msg)
    h.hexdigest()


# Python内置的hmac模块实现了标准的Hmac算法，
# 它利用一个key对message计算“杂凑”后的hash，
# 使用hmac算法比标准hash算法更安全，
# 因为针对相同的message，不同的key会产生不同的hash。

if __name__ == '__main__':
    md5CurrPy()
    # shaCurrpy()
