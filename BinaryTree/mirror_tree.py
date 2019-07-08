# -*- coding:utf-8 -*-

""" 操作给定的二叉树，将其变换为源二叉树的镜像
    如:
                8                                      8
         6            10          ===>        10               6
    5       7      9       11             11       9       7        5

"""

""" 思路 使用递归 将每个根节点的左右节点交换"""
from BinaryTree.base_tree_node import gen_a_tree


def mirror(root_node):

    if root_node:
        tmp = root_node.left
        root_node.left = root_node.right
        root_node.right = tmp
        if root_node.left:
            mirror(root_node.left)
        if root_node.right:
            mirror(root_node.right)
    else:
        return None


if __name__ == '__main__':

    root = gen_a_tree()
    print(mirror(root))