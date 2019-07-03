# -*- coding:utf-8 -*-

""" 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的,
    也不知道每个数字重复几次。请找出数组中第一个重复的数字。
    例如，如果输入长度为7的数组[2,3,1,0,2,5,3]，那么对应的输出是第一个重复的数字2。"""

""" 思路 遍历原始数组 添加新元素到新数组 同时判断元素如果在新数组中 就说明已重复 返回此元素即可"""


def first_repeat_num(a):

    new = []
    for i in range(len(a)):
        if a[i] in new:
            return a[i]
        else:
            new.append(a[i])


if __name__ == '__main__':

    l = [2,3,1,0,2,5,3]
    print(first_repeat_num(l))