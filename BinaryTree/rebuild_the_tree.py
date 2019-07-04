# -*- coding:utf-8 -*-

""" 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
    假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
    例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""

""" 思路 递归"""

from BinaryTree.base_tree_node import TreeNode, dlr_print_2


def tree(dlr, ldr):
    """
    :param dlr:  前序遍历序列
    :param ldr:  中序遍历序列
    :return:
    """
    if len(dlr) == 0:
        return None
    elif len(dlr) == 1:
        return TreeNode(dlr[0])
    else:
        degree_node = TreeNode(dlr[0])
        mid = ldr.index(dlr[0])
        degree_node.left = tree(dlr[1:mid+1], ldr[:mid])
        degree_node.right = tree(dlr[mid+1:], ldr[mid:])

    return degree_node


if __name__ == '__main__':

    dlr_list = [1, 2, 4, 7, 3, 5, 6, 8]
    ldr_list = [4, 7, 2, 1, 5, 3, 8, 6]
    result = tree(dlr_list, ldr_list)
    # print(result)
    dlr_print_2(result)
