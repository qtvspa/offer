# -*- coding:utf-8 -*-

""" 复制复杂链表
    输入一个复杂链表，每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点
    返回结果为复制后复杂链表的head。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空） """

""" 基本思路 
    第一步：复制复杂指针的label和next。但是这次我们把复制的结点跟在元结点后面，而不是直接创建新的链表；
    第二步：设置复制出来的结点的random。因为新旧结点是前后对应关系，所以也是一步就能找到random；
    第三步：拆分链表。奇数是原链表，偶数是复制的链表。"""

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# 第一步，复制复杂指针的label和next
def clone_first(pHead):

    pNode = pHead
    while pHead:
        pClone = RandomListNode(0)
        pClone.label = pNode.label
        pClone.next = pNode.next
        pClone.random = None
        pNode.next = pClone
        pNode = pClone.next


# 第二步，处理复杂指针的random
def clone_second(pHead):

    pNode = pHead
    while pNode:
        pClone = pNode.next
        if pNode.random:
            pClone.random = pNode.random.next
        pNode = pClone.next



# 第三步，拆分复杂指针
def clone_third(pHead):

    pNode = pHead
    pCloneNode = None
    pCloneHead = None

    if pNode:
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next

    while pNode:
        pCloneNode.next = pNode.next
        pCloneNode = pCloneNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next

    return pCloneHead


# 更好的方法
class Solution:
    def Clone(self, head):
        if not head:
            return
        newNode = RandomListNode(head.label)
        newNode.random = head.random
        newNode.next = self.Clone(head.next)
        return newNode