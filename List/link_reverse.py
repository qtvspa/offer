# -*- coding:utf-8 -*-

""" 反转链表 """

""" 思路
    设定三个指针 分别指向当前节点 当前节点的前一节点 当前节点的后一节点
    遍历时 首先临时存储当前节点的后一节点 然后把当前节点的后一节点指向前一节点、前一节点=当前节点、当前节点=后一节点"""

from List.linklist_base import LinkList


def list_reverse(link_list):

    if not link_list.head:
        return link_list

    p_head = link_list.head
    p_last = None

    while p_head:
        tmp = p_head.next
        p_head.next = p_last
        p_last = p_head
        p_head = tmp

    return p_last


if __name__ == '__main__':

    l = LinkList()
    l.init_list([1, 3, 6, 5, 8])
    head = list_reverse(l)
    while head:
        print(head.data)
        head = head.next
