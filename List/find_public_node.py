# -*- coding:utf-8 -*-

""" 输入两个链表 找到它们的第一个公共节点"""

""" 思路
    
    方法一：
    可以把两个链表拼接起来，一个pHead1在前pHead2在后，一个pHead2在前pHead1在后。
    这样，生成了两个相同长度的链表，那么我们只要同时遍历这两个表，就一定能找到公共结点。时间复杂度O(m+n)，空间复杂度O(m+n)。

    方法二：
    也可以先让把长的链表的头砍掉，让两个链表长度相同，这样，同时遍历也能找到公共结点。
    此时，时间复杂度O(m+n)，空间复杂度为O(MAX(m,n))。

"""
from List.linklist_base import LinkList


# 使用方法二
def find_public_node(l1, l2):

    l1_head = l1.head
    l2_head = l2.head

    if not l1:
        return None
    if not l2:
        return None

    len1 = l1.get_length()
    len2 = l2.get_length()

    # 先假设l1较长
    len_dif = len1 - len2
    if len_dif < 0:
        len_dif = len2 - len1
        for _ in range(len_dif):
            l2_head = l2_head.next
        for _ in range(len1):
            if l1_head.data == l2_head.data:
                return l1_head.data
            else:
                l1_head = l1_head.next
                l2_head = l2_head.next
    else:
        for _ in range(len_dif):
            l1_head = l1_head.next

        for _ in range(len2):
            if l1_head.data == l2_head.data:
                return l1_head.data
            else:
                l1_head = l1_head.next
                l2_head = l2_head.next


if __name__ == '__main__':

    l1 = LinkList()
    l2 = LinkList()
    l1.init_list([1, 9, 7, 10, 3, 4])
    l2.init_list([2, 6, 10, 3, 4])
    result = find_public_node(l1, l2)
    print(result)