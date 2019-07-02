# -*- coding:utf-8 -*-

""" 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
    例如输入一个长度为9的数组[1,2,3,2,2,2,5,4,2]。
    由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。"""

""" 思路 用字典保存各元素出现的次数即可"""

import numpy as np


def find_the_num(li):

    info = {}
    length = len(li)
    if not length:
        return 0
    for i in range(length):
        if li[i] in info.keys():
            info[li[i]] += 1
        else:
            info[li[i]] = 1

    for k, v in info.items():
        if v > length / 2:
            return k


if __name__ == '__main__':

    a = np.array([1,2,3,2,2,2,5,4,2])
    result = find_the_num(a)
    print(result)