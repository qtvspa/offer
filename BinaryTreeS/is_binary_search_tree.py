# -*- coding:utf-8 -*-

""" 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
    如果是则输出Yes，否则输出No。假设输入的数组的任意两个数字都互不相同。"""

""" 思路 根据二叉搜索树的性质：左子树value < 根节点value < 右子树value
    递归判断数组中元素 是否符合该性质
"""

def is_binary_search_tree(l):

    length = len(l)
    if length <= 1:
        return True
    left = []
    right = []
    root = l[length-1]
    for i in l:
        if i < root:
            left.append(i)
        elif i > root:
            right.append(i)
    if not all((left, right)):
        return False

    return is_binary_search_tree(left) and is_binary_search_tree(right)


if __name__ == '__main__':

    li = [5, 7, 6, 9, 11, 10, 8]
    print(is_binary_search_tree(li))