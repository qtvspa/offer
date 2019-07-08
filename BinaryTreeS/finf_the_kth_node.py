# -*- coding:utf-8 -*-

""" 给定一颗二叉搜索树，请找出其中的第k大的结点。"""

""" 思路 中序遍历即可"""
from BinaryTree.base_tree_node import gen_a_tree


def ldr(root):

    li = []
    if not root:
        return []
    else:
        li += ldr(root.left)
        li.append(root.value)
        li += ldr(root.right)

    return li

if __name__ == '__main__':

    r = gen_a_tree()
    k = 3

    result = ldr(r)
    print(result[k-1])