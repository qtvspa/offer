# -*- coding:utf-8 -*-

""" 一个整型数组里除了两个数字之外，其他的数字都出现了两次。
    请写程序找出这两个只出现一次的数字。"""

""" 思路 1
    直接遍历数组，用字典存储每个元素出现的次数，最后提取字典中value为1的两个key即可

    思路 2 (比1复杂)
    先将数组分成两个子数组 每个子数组各包含一个只出现一次的数字
    
    重点 从头到尾依次异或数组中的每一个数字，那么最终得到的结果就是两个只出现一次的数字的异或结果。
        因为其它数字都出现了两次，在异或中全部抵消掉了。由于这两个数字肯定不一样，那么这个异或结果肯定不为0，
        也就是说在这个结果数字的二进制表示中至少就有一位为1 。我们在结果数字中找到第一个为1的位的位置，记为第N位。
        接下来以第N位是不是1为标准把原数组中的数字分成两个子数组，第一个子数组中每个数字的第N位都为1 ，而第二个子数组的每个数字的第N位都为0 。
        现在我们已经把原数组分成了两个子数组，每个子数组都包含一个只出现一次的数字，而其它数字都出现了两次
    
    然后对子数组使用异或 判断某一数组元素是否有重复值
    异或 1^1=0 1^0=0 0^1=1 0^0=0
"""


def get_the_once(a):

    len_a = len(a)
    result = 0
    x = 0
    y = 0
    n = 0
    for i in range(len_a):
        result ^= a[i]

    result_b = bin(result).replace('0b', '')
    result_b = result_b[::-1]
    for i, j in enumerate(result_b):
        if j == '1':
            n = i
    a_list = []
    b_list = []
    for i in range(len_a):
        s = bin(a[i]).replace('0b', '')[::-1]
        if len(s) > n and s[n] == '1':
            print(bin(a[i]).replace('0b', '')[::-1])
            a_list.append(a[i])
        else:
            b_list.append(a[i])

    print(a_list, b_list)
    for i in range(len(a_list)):
        x ^= a_list[i]
    for i in range(len(b_list)):
        y ^= b_list[i]

    return x, y


if __name__ == '__main__':

    aa = [1, 2, 2, 7, 7, 5, 3, 5, 3, 4]
    print(get_the_once(aa))