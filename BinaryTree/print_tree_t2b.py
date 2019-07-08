# -*- coding:utf-8 -*-

""" 从上往下打印出二叉树的每个节点，同层节点从左至右打印。 """

""" 思路 遍历时 使用一个队列来存储将要打印的结点 利用先进先出的特点 依次打印队列中的元素"""


from queue import Queue
from BinaryTree.base_tree_node import gen_a_tree


def top2bottom_print(root):

    if not root:
        return []
    task = Queue()
    task.put(root)
    result = []

    while not task.empty():
        node = task.get()
        root = node
        result.append(node.value)

        if root.left:
            task.put(root.left)
        if root.right:
            task.put(root.right)
    return result


if __name__ == '__main__':

    root_node = gen_a_tree()
    res = top2bottom_print(root_node)
    print(res)