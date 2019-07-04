# -*- coding:utf-8 -*-

""" 请实现一个函数用来判断字符串是否表示数值（包括整数和小数
    例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
    但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。"""

""" 思路 考虑好各种情况即可"""


def is_number(s):

    l = len(s)

    for i in range(l):
        while i == 0:
            if s[i] in ['-', '+']:
                break
            elif s[i] in ['1','2','3','4','5','6','7','8','9']:
                break
            else:
                return False
        while i > 0:
            if s[i] in ['e', 'E']:
                if i + 1 < l:
                    ss = s[i+1:]
                    for j in range(len(ss)):
                        if j == 0:
                            if ss[j] not in ['-', '+']:
                                return False
                            else:
                                continue
                        else:
                            if ss[j] not in ['1','2','3','4','5','6','7','8','9']:
                                return False
                            if j+1 == len(ss):
                                return True
                else:
                    return False
            elif s[i] == '.':
                break
            elif s[i] in ['1','2','3','4','5','6','7','8','9']:
                break
            else:
                return False

    return True



if __name__ == '__main__':

    s1 = '-1E-16'
    s2 = '12e+4.36'
    print(is_number(s1))
    print(is_number(s2))