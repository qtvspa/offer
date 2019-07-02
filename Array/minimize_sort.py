# -*- coding:utf-8 -*-


""" 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
    例如输入数组[3，32，321]，则打印出这三个数字能排成的最小数字为321323。"""

""" 思路 将组合成的数字转化为字符串 再进行比较"""

import numpy as np
import functools

def mini_sort(numbers):

    if not len(numbers):
        return ""
    lmb = lambda n1, n2: int(str(n1) + str(n2)) - int(str(n2) + str(n1))
    array = sorted(numbers, key=functools.cmp_to_key(lmb))
    print(array)
    return ''.join([str(i) for i in array])


if __name__ == '__main__':

    a = np.array([3, 32, 321])
    result = mini_sort(a)
    print(result)