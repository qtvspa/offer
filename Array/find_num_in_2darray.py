# -*- coding:utf-8 -*-

""" 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
    请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。"""


""" 思路
    首先选取数组中右上角的数字。如果该数字等于要查找的数字，查找过程结束；
    如果该数字大于要查找的数组，剔除这个数字所在的列；
    如果该数字小于要查找的数字，剔除这个数字所在的行。
    直到找到要查找的数字，或者查找范围为空。"""

import numpy as np


def find_the_num(array, target_num):

    row, column = array.shape
    if row > 0 and column > 0:
        x = 0
        y = column - 1
        while x < row and y >= 0:
            if array[x][y] > target_num:
                y -= 1
            elif array[x][y] < target_num:
                x += 1
            else:
                return True
    return False


if __name__ == '__main__':

    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(find_the_num(a, 8))