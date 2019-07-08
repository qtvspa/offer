# -*- coding:utf-8 -*-

""" 实现fibonacci数列"""



def fibonacci(num):

    a, b = 0, 1
    count = 0
    while count < num:
        a, b = b, a+b
        count += 1
        yield a


if __name__ == '__main__':

    print([i for i in fibonacci(10)])