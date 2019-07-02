# -*- coding:utf-8 -*-

""" 一个链表中包含环，请找出该链表的环的入口结点。"""

""" 思路
    首先计算出环的长度k：使用快慢指针法。一个走两步，一个走一步， 直到两个指针相遇。相遇位置一定在环中。
    由此位置边遍历边计数，当回到此位置时，即可得到环的长度。
    再设定两个指针，第一个指针先走k步，然后两个指针一起走，直到相遇。此时相遇的位置即为入口结点。
"""
from List.linklist_base import LinkList


def find_entrance(l1):
    node1 = l1.head
    node2 = l1.head

    if not node1:
        return None
    meeting_node = None
    i = 0
    while True:
        node1 = node1.next
        if i % 2 == 1:
            node2 = node2.next
        if node1 == node2:
            meeting_node = node2
            break
        i += 1
    if not meeting_node:
        return None

    start_node = meeting_node
    count = 0
    while True:
        meeting_node = meeting_node.next
        count += 1
        if meeting_node == start_node:
            break

    first = l.head
    later = l.head
    for _ in range(count):
        first = first.next
    while True:
        if first == later:
            return later.data
        else:
            later = later.next
            first = first.next


if __name__ == '__main__':

    # 初始化一个带环的链表
    l = LinkList()
    l.init_list([1, 3, 4, 5, 6, 9])
    head = l.head
    target_node = head.next.next

    for _ in range(l.get_length()):
        if not head.next:
            head.next = target_node
        else:
            head = head.next

    result = find_entrance(l)
    print(result)