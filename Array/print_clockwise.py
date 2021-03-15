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
""" 思路 定义四个边界 遍历二维数组即可 需要考虑边界条件"""


def clockwise_print(matrix):
    m, n = len(matrix), len(matrix[0])
    top, bottom, left, right = 0, m, 0, n
    ans = []

    while bottom > top and right > left:
        for i in range(left, right):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom):
            ans.append(matrix[i][right - 1])
        right -= 1

        for i in range(right, left, -1):
            if bottom > top:
                ans.append(matrix[bottom - 1][i - 1])
        bottom -= 1

        for i in range(bottom, top, -1):
            if right > left:
                ans.append(matrix[i - 1][left])
        left += 1

    return ans


if __name__ == '__main__':
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    b = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    print(clockwise_print(a))
