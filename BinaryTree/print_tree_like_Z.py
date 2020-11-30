# -*- coding:utf-8 -*-

from BinaryTree.base_tree_node import gen_a_tree

""" 请实现一个函数按照Z字形打印二叉树，即第一行按照从左到右的顺序打印，
    第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。"""


""" 思路 
    定义两个列表 一个用来存储当前层的值value_list 另一个用来存储下一层的node_list
    获取到当前层value的同时将下一层的所有节点存入node_list
    每次遍历node_list 直到此列表为空为止 
    初始node_list为一个包含根节点的list
"""


def z_print(root_node):

    data = []
    if not root_node:
        return data
    tmp = [root_node]

    flag = True
    while tmp:
        current_values = []
        next_layer_nodes = []
        flag = not flag

        for node in tmp:
            current_values.append(node.value)
            if node.left:
                next_layer_nodes.append(node.left)
            if node.right:
                next_layer_nodes.append(node.right)

        tmp = next_layer_nodes

        if flag:
            data.append(current_values[::-1])
        else:
            data.append(current_values)

    return data


if __name__ == '__main__':

    root = gen_a_tree()

    result = z_print(root)
    print(result)
