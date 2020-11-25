# -*- coding:utf-8 -*-


""" 统计一个数字在一个已排序数组中出现的次数"""

""" 思路 二分法 递归实现 时间复杂度O(logN)"""


def get_the_count(a, target):
    """
    :param a: a list of sorted numbers
    :param target: the number to be counted
    :return:
    """
    tmp = []
    count = 0
    if target in a:
        a_len = len(a)
        l = int(a_len/2)
        if target == a[l]:
            i = l - 1
            j = l + 1
            count = 1
            while i > 0:
                if a[i] == target:
                    count += 1
                i -= 1
            while j < a_len:
                if a[j] == target:
                    count += 1
                j += 1
            return count
        elif target > a[l] and count == 0:
            tmp = a[l:]
        elif target < a[l] and count == 0:
            tmp = a[:l]

    return get_the_count(tmp, target)


if __name__ == '__main__':

    aa = [1, 2, 2, 3, 3, 3, 5, 8, 9]
    # 可直接使用print(aa.count(2))
    result = get_the_count(aa, 3)
    print(result)
