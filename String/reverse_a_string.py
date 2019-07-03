# -*- coding:utf-8 -*-

""" 反转字符串 输入what is your name 输出name your is what"""

if __name__ == '__main__':

    ss = 'what is your name'
    print(' '.join(ss.split(' ')[:: -1]))