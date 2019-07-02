# -*- coding:utf-8 -*-


""" 输出链表的倒数第k个节点"""

""" 思路
    定义两个指针 先让第一个指针走k-1步 使两个指针保持k的距离
    然后两个指针一起走 直到第一个指针走到链表末尾 第二个指针此时所指向的位置即为倒数第k个节点位置"""


from LIST.linklist_base import LinkList


def find_kth_node_from_last(link_list, k):

    if link_list.is_empty() or k == 0:
        return None
    p_head = link_list.head
    p_behind = link_list.head

    for i in range(k-1):
        if p_head.next:
            p_head = p_head.next
        else:
            return None
    while p_head.next is not None:
        p_behind = p_behind.next
        p_head = p_head.next

    return p_behind


if __name__ == '__main__':

    l = LinkList()
    l.init_list([1, 5, 8, 9, 23, 4, 10])
    result = find_kth_node_from_last(l, 3)
    print(result.data)