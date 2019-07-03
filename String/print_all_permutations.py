# -*- coding:utf-8 -*-

""" 输入一个字符串,按字典序打印出该字符串中字符的所有排列。
    例如输入字符串abc，则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。"""

""" 思路 递归实现"""


def permutations(arr, position, end):

    if position == end:
        print(''.join(arr))

    else:
        for index in range(position, end):
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            arr[index], arr[position] = arr[position], arr[index]


if __name__ == '__main__':

    ss = 'abc'
    a = list(ss)

    permutations(a, 0, len(a))

