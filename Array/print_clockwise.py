# -*- coding:utf-8 -*-

import numpy as np

""" 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
    例如，如果输入如下矩阵
    [1, 2, 3, 4
     5, 6, 7, 8
     9, 10, 11, 12
     13, 14, 15, 16]
    应打印 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

"""
""" 思路 定义四个边界 遍历二维数组即可"""


def clockwise_print(array):
    row, column = array.shape

    top, bottom, left, right = 0, row, 0, column
    tmp_list = []
    while bottom > top and right > left:
        top1, bottom1, left1, right1 = top, bottom, left, right
        for i in range(left1, right1):
            tmp_list.append(array[top1][i])
        top1 += 1
        for j in range(top1, bottom1):
            tmp_list.append(array[j][right1-1])
        right1 -= 1
        while right1 > left1:
            tmp_list.append(array[bottom1-1][right1-1])
            right1 -= 1
        bottom1 -= 1
        while bottom1 > top1:
            tmp_list.append(array[bottom1-1][left1])
            bottom1 -= 1
        left1 += 1

        top += 1
        bottom -= 1
        left += 1
        right -= 1

    return tmp_list


if __name__ == '__main__':

    a = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
    b = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
    print(clockwise_print(b))
