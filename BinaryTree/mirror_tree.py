# -*- coding:utf-8 -*-

from BinaryTree.base_tree_node import gen_a_tree

""" 操作给定的二叉树，将其变换为源二叉树的镜像
    如:
                8                                      8
         6            10          ===>        10               6
    5       7      9       11             11       9       7        5

"""

""" 
    思路一 使用递归 将每个根节点的左右节点交换
    思路二 使用栈(列表)保存每个根结点 然后逐一交换字节点
"""


def mirror(root_node):
    """ 递归 """

    if root_node:
        root_node.left, root_node.right = root_node.right, root_node.left
        if root_node.left:
            mirror(root_node.left)
        if root_node.right:
            mirror(root_node.right)
    else:
        return None


def mirror2(root_node):
    """ 非递归 """

    if root_node:
        tmp_list = [root_node]
        while tmp_list:
            node = tmp_list.pop(0)
            if node:
                tmp_list.append(node.left)
                tmp_list.append(node.right)
                node.left, node.right = node.right, node.left
    return None


if __name__ == '__main__':

    root = gen_a_tree()
    print(mirror(root))
