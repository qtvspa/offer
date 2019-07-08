# -*- coding:utf-8 -*-

""" 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。"""

from BinaryTree.base_tree_node import gen_a_tree


def print_multi(root_node):
    # 非递归方法
    result = []
    if not root_node:
        return []
    data = [root_node]
    while data:
        node_values = []
        next_layer_nodes = []
        for node in data:
            if node.left:
                next_layer_nodes.append(node.left)
            if node.right:
                next_layer_nodes.append(node.right)
            node_values.append(node.value)

        data = next_layer_nodes
        result.append(node_values)

    return result


def print_multi_2(root_node_list):

    # 递归方法
    if not root_node_list:
        return

    node_values = []
    next_layer_nodes = []
    for node in root_node_list:
        if node.left:
            next_layer_nodes.append(node.left)
        if node.right:
            next_layer_nodes.append(node.right)
        node_values.append(node.value)

    print(node_values)
    print_multi_2(next_layer_nodes)

    return next_layer_nodes



if __name__ == '__main__':

    root = gen_a_tree()

    for i in print_multi(root):
        print(i, '\n')

    print_multi_2([root])