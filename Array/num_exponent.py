# -*- coding:utf-8 -*-

""" 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。"""

""" 思路 
    注意浮点数可能为0"""


def expo(num, exponent):

    # # 指数奇偶性
    # flag = 0
    # if exponent % 2:
    #     flag = 1
    result = num
    if num < 0:
        num = abs(num)
        for i in range(exponent-1):
            result *= num
        return 0 - result
    elif num > 0:
        for i in range(exponent-1):
            result *= num
        return result
    else:
        return result


if __name__ == '__main__':

    res = round(expo(1.44, 3), 3)
    print(res)