# -*- coding:utf-8 -*-

""" 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
    示例:
    输入:
    [
      1->4->5,
      1->3->4,
      2->6
    ]
    输出: 1->1->2->3->4->4->5->6
"""

from List.linklist_base import ListNode


def merge_2_list(head1, head2):

    if not head1:
        return head2
    if not head2:
        return head1

    if head1.data < head2.data:
        result_head = head1
        result_head.next = merge_2_list(head1.next, head2)
    else:
        result_head = head2
        result_head.next = merge_2_list(head1, head2.next)
    return result_head


# 逐一两两合并  此方法时间复杂度为O（KN） 空间复杂度O（1）
# def merge_k_lists(lists) -> ListNode:
#
#     if not lists:
#         return ListNode(0).next
#
#     head1 = lists.pop(0)
#     while lists:
#         head2 = lists.pop(0)
#         head1 = merge_2_list(head1, head2)
#
#     return head1

# 分治法 使用归并 此方法时间复杂度为O（NlogK） 空间复杂度O（1）
# def merge_k_lists(lists) -> ListNode:
#
#     amount = len(lists)
#     interval = 1
#     while interval < amount:
#         for i in range(0, amount - interval, interval * 2):
#             lists[i] = merge_2_list(lists[i], lists[i + interval])
#         interval *= 2
#     return lists[0] if amount > 0 else lists

# 使用优先级队列 借助heapq 此方法时间复杂度为O（NlogK） 空间复杂度O（N）
def merge_k_lists(lists) -> ListNode:

    import heapq
    dummy = ListNode(0)
    p = dummy
    head = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(head, (lists[i].data, i))
            lists[i] = lists[i].next
    while head:
        val, idx = heapq.heappop(head)
        p.next = ListNode(val)
        p = p.next
        if lists[idx]:
            heapq.heappush(head, (lists[idx].data, idx))
            lists[idx] = lists[idx].next
    return dummy.next


if __name__ == '__main__':

    node1_1 = ListNode(1)
    node1_2 = ListNode(4)
    node1_3 = ListNode(5)
    node1_1.next = node1_2
    node1_2.next = node1_3

    node2_1 = ListNode(1)
    node2_2 = ListNode(3)
    node2_3 = ListNode(4)
    node2_1.next = node2_2
    node2_2.next = node2_3

    node3_1 = ListNode(2)
    node3_2 = ListNode(6)
    node3_1.next = node3_2

    input_list = [node1_1, node2_1, node3_1]
    result = merge_k_lists(input_list)

    while result:
        print(result.data)
        result = result.next

