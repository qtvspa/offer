# -*- coding:utf-8 -*-

""" 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
    注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。"""

""" 思路 根据给定二叉树节点所在的位置
    
    首先判断有无右子节点
        如果有 则返回右子节点的最左子节点
        如果没有 
            若此节点为父节点的左子节点 则直接返回父节点
            若此节点为父节点的右子节点   
                需要沿着指向父节点的指针一直向上遍历 直到找到一个身为左子节点的节点
                如果这样的节点存在 那么这个节点的父节点就是我们要找的下一个节点
                
"""


class TreeNodeSp:
    def __init__(self, x):
        self.value = x
        self.parent = None
        self.left = None
        self.right = None


def gen_a_tree_sp():
    """ 生成一个测试用例"""

    node1 = TreeNodeSp(1)
    node2 = TreeNodeSp(2)
    node3 = TreeNodeSp(3)
    node4 = TreeNodeSp(4)
    node5 = TreeNodeSp(5)
    node6 = TreeNodeSp(6)
    node7 = TreeNodeSp(7)
    node8 = TreeNodeSp(8)
    node9 = TreeNodeSp(9)

    node1.left = node2
    node2.parent = node1
    node1.right = node3
    node3.parent = node1
    node2.left = node4
    node4.parent = node2
    node2.right = node5
    node5.parent = node2
    node3.left = node6
    node6.parent = node3
    node3.right = node7
    node7.parent = node3
    node5.left = node8
    node8.parent = node5
    node5.right = node9
    node9.parent = node5

    return node1


def find_the_node(node):

    if not node:
        return None
    if node.right:
        tmp = node.right
        while tmp.left:
            tmp = tmp.left
        return tmp

    else:
        if not node.parent:
            return None
        else:
            if node == node.parent.left:
                return node.parent
            elif node == node.parent.right:
                p = node.parent
                while p:
                    if p.parent:
                        if p == p.parent.left:
                            return p.parent
                        else:
                            p = p.parent


if __name__ == '__main__':

    the_node = gen_a_tree_sp()
    result = find_the_node(the_node.left.right.right)
    print(result.value)





