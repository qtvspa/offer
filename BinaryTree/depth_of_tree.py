# -*- coding:utf-8 -*-

from BinaryTree.base_tree_node import gen_a_tree

""" 输入一棵二叉树，求该树的深度"""

""" 思路 DFS/BFS"""


def dfs(root):

    if not root:
        return 0

    left = dfs(root.left)
    right = dfs(root.right)

    return max(left, right) + 1


def bfs(root):

    # bfs遍历 利用队列将每层的跟节点逐一打印
    if not root:
        return 0
    my_queue = []
    node = root
    my_queue.append(node)

    while my_queue:
        node = my_queue.pop(0)
        print(node.value)
        if node.left is not None:
            my_queue.append(node.left)
        if node.right is not None:
            my_queue.append(node.right)


if __name__ == '__main__':

    a = gen_a_tree()
    print(dfs(a))
    # bfs(a)
