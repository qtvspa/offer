# -*- coding:utf-8 -*-

""" 在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置。"""

""" 思路 遍历第一遍时用字典存每个字符串出现的次数 第二遍遍历 同时在字典中的value如果为1 则返回"""


def once(ss):

    ss = list(ss)
    info = {}

    for i in ss:
        if i in info.keys():
            info[i] += 1
        else:
            info[i] = 1
    for i, v in enumerate(ss):
        if info[v] == 1:
            return ss[i]


if __name__ == '__main__':

    print(once('qwwqedjjlsvhsdkhvg'))