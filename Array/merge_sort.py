# -*- coding:utf-8 -*-

""" 归并排序"""

""" 思路 
    将数组按照middle进行递归拆分，最后分到最细之后，再每个子数组其进行排序。使用下面的方法：
    
    同时对两个数组的第一个位置进行比大小，将小的放入一个空数组，然后被放入空数组的那个位置的指针往后移一位，
    然后继续和另外一个数组的上一个位置进行比较，以此类推。到最后任何一个数组先出栈完，就将另外一个数组里的所有元素追加到新数组后面。

    由于递归拆分的时间复杂度是logN，进行两个有序数组排序的方法复杂度是N，故该算法的时间复杂度是N*logN。
"""


def merge(a, b):
    tmp = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            tmp.append(a[j])
            j += 1
        else:
            tmp.append(b[h])
            h += 1

    if j == len(a):
        for i in b[h:]:
            tmp.append(i)
    else:
        for i in a[j:]:
            tmp.append(i)

    return tmp


def merge_sort(lists):

    if len(lists) <= 1:
        return lists

    middle = len(lists)/2
    left = merge_sort(lists[: int(middle)])
    right = merge_sort(lists[int(middle): ])

    return merge(left, right)


if __name__ == '__main__':

    aa = [4, 7, 8, 3, 5, 9]
    print(merge_sort(aa))