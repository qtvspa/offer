# -*- coding:utf-8 -*-

from BinaryTree.base_tree_node import gen_a_tree, TreeNode

""" 输入两颗二叉树A，B，判断B是不是A的子结构。（约定空树不是任意一个树的子结构）"""

""" 思路 
    要查找树A中是否存在和树B结构一样的子树，可以分为两步：
    第一步在树A中找到和B的根结点的值一样的结点R
    第二步再判断树A中以R为根节点的子树是不是包含和树B一样的结构。
"""


def is_subtree(a, b):
    if not b:
        return True
    if not a or a.value != b.value:
        return False
    return is_subtree(a.left, b.left) and is_subtree(a.right, b.right)


def has_subtree(a, b):
    if not a or not b:
        return False
    return has_subtree(a.left, b) or has_subtree(a.right, b) or is_subtree(a, b)


if __name__ == '__main__':

    b_node1 = TreeNode(3)
    b_node2 = TreeNode(6)
    b_node3 = TreeNode(7)
    b_node1.left = b_node2
    b_node1.right = b_node3

    a_node = gen_a_tree()

    print(has_subtree(a_node, b_node1))
