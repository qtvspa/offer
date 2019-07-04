# -*- coding:utf-8 -*-


""" 输入一棵二叉树和一个整数，打印出二叉树中结点值的和为该整数的所有路径。
    路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。"""

from BinaryTree.base_tree_node import gen_a_tree


def path(a, num):

    if not a:
        return []
    if not a.left and not a.right and a.value == num:
        return [[a.value]]

    res = []
    left = path(a.left, num - a.value)
    right = path(a.right, num - a.value)

    for i in left + right:
        res.append([a.value] + i)
    return res


if __name__ == '__main__':

    root = gen_a_tree()
    print(path(root, 8))


