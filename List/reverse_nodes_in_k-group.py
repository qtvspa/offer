# -*- coding:utf-8 -*-

""" 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。
    如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

    示例 :
        给定这个链表：1->2->3->4->5
        当 k = 2 时，应当返回: 2->1->4->3->5
        当 k = 3 时，应当返回: 3->2->1->4->5

    说明 :
        你的算法只能使用常数的额外空间。
        你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""


from List.linklist_base import LinkList, ListNode


def reverse_k_group(head: ListNode, k: int) -> ListNode:

    start_node = ListNode(0)
    p = start_node
    while True:
        the_stack = []
        tmp = head
        count = k
        while tmp and count:
            the_stack.append(tmp)
            tmp = tmp.next
            count -= 1

        if count:
            p.next = head
            break

        while the_stack:
            p.next = the_stack.pop()
            p = p.next

        p.next = tmp
        head = tmp

    return start_node.next


if __name__ == '__main__':

    the_list = LinkList()
    the_list.init_list([1, 2, 3, 4, 5])
    the_head = the_list.head
    result = reverse_k_group(the_head, 2)
    while result:
        print(result.data)
        result = result.next




