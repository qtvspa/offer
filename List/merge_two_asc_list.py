# -*- coding:utf-8 -*-

""" 合并两个有序递增的链表 """

""" 首先 特殊情况要考虑: 1空2非空 1非空2空 12皆空
    使用递归 从头遍历链表 判断当前指针 哪个链表中的值小 即赋给合并链表指针即可"""


from LIST.linklist_base import LinkList


def merge(l1_head, l2_head):

    if not l2_head:
        return l1_head
    if not l1_head:
        return l2_head

    if l1_head.data < l2_head.data:
        merge_head = l1_head
        merge_head.next = merge(l1_head.next, l2_head)
    else:
        merge_head = l2_head
        merge_head.next = merge(l1_head, l2_head.next)
    return merge_head


if __name__ == '__main__':

    l1 = LinkList()
    l1.init_list([1, 2, 3])
    l2 = LinkList()
    l2.init_list([1, 4, 5, 6])
    result = merge(l1.head, l2.head)

    while result:
        print(result.data)
        result = result.next