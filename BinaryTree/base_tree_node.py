# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def add(root, data):
    """ 提供根节点和新的值 向一棵树添加新节点"""
    node = TreeNode(data)

    if not root.value:
        root = node
    else:
        my_queue = []
        root_node = root
        my_queue.append(root_node)

        # 对已有的节点进行层次遍历
        while my_queue:
            tree_node = my_queue.pop(0)
            if not tree_node.left:
                tree_node.left = node
                return
            elif not tree_node.right:
                tree_node.right = node
                return
            else:
                my_queue.append(tree_node.left)
                my_queue.append(tree_node.right)
    return root


def dlr_print(tree):
    """ 前序遍历 """
    if not tree:
        return None
    else:
        print(tree.value)
        dlr_print(tree.left)
        dlr_print(tree.right)


def dlr_print_2(root):
    """ 非递归前序遍历 """
    if not root:
        return
    my_stack = [root]
    node = root
    while my_stack or node:
        while node:  # 从根节点开始，一直寻找他的左子树
            print(node.value)
            my_stack.append(node)
            node = node.left
        node = my_stack.pop()    # while结束表示当前节点node为空，即前一个节点没有左子树了
        node = node.right       # 开始查看它的右子树


def ldr_print(tree):
    """ 中序遍历 """
    if not tree:
        return None
    else:
        dlr_print(tree.left)
        print(tree.value)
        dlr_print(tree.right)


def lrd_print(tree):
    """ 后序遍历 """
    if not tree:
        return None
    else:
        dlr_print(tree.left)
        dlr_print(tree.right)
        print(tree.value)


def gen_a_tree():
    """ 生成一个测试用的二叉树结构"""
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7

    return node1