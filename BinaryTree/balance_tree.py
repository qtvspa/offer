# -*- coding:utf-8 -*-

from BinaryTree.base_tree_node import gen_a_tree

""" 输入一棵二叉树，判断该二叉树是否是平衡二叉树。 """

""" 思路 此处只需判断一条性质: 任意节点的左右子树高度差不超过1 
    ps（AVL平衡二叉搜索树还要加上 任意节点左子树的value < 根节点value < 右子树value）
    
    用后序遍历的方式遍历二叉树的每一个结点，在遍历到一个结点之前我们就已经遍历了它的左右子树。
    只要在遍历每个结点的时候记录它的深度，就可以一边遍历一边判断每个结点是不是平衡的。
"""


def depth_of_tree(root):

    if not root:
        return -1
    left = depth_of_tree(root.left)
    right = depth_of_tree(root.right)

    return max(left, right) + 1


def is_balance(root):

    if not root:
        return False
    else:
        left = depth_of_tree(root.left)
        right = depth_of_tree(root.right)

    if abs(left - right) > 1:
        return False
    return True


if __name__ == '__main__':

    node = gen_a_tree()

    print(depth_of_tree(node))
    print(is_balance(node))
