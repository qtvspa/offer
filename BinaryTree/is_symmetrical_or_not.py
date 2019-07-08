# -*- coding:utf-8 -*-

""" 请实现一个函数，用来判断一颗二叉树是不是对称的。"""

""" 思路 
    首先求出此二叉树的镜像
    然后判断原二叉树与镜像是否相等 如果相等 即为对称
"""

from BinaryTree.base_tree_node import gen_a_tree, TreeNode
from BinaryTree.mirror_tree import mirror  # 之前写过的镜像函数


def symmetrical(node, mirror_node):

    if not node and not mirror_node:
        return True
    elif not all((node, mirror_node)):
        return False
    else:
        if node.value == mirror_node.value:
            return symmetrical(node.left, node.left) and symmetrical(node.left, node.right)
        else:
            return False


if __name__ == '__main__':

    root = gen_a_tree()  # root为非对称的测试用例
    root2 = gen_a_tree()
    mir = mirror(root2)

    print(symmetrical(root, root2))

    root3 = TreeNode(1) # root3为对称的测试用例
    node1 = TreeNode(2)
    node2 = TreeNode(2)
    root3.left = node1
    root3.right = node2

    root4 = root3
    mirror(root4)
    print(symmetrical(root3, root4))