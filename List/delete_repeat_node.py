# -*- coding:utf-8 -*-

"""
    在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
    例如，链表1->2->3->3->4->4->5 处理后为 1->2->5。
"""

""" 思路
    需要记录当前结点前的最近访问过的不重复结点pre_node、当前结点cur_node、以及指向cur_node后面的结点next_node
    如果cur_node和它后面的几个结点数值相同，那么这些结点都要被剔除，然后更新pre_node和cur_node；如果不相同，则直接更新pre_node和cur_node。
    如果第一个结点是重复结点，那么就把头指针head_node也更新一下。
"""

from List.linklist_base import LinkList


def delete_repeated_node(li):

    head_node = li.head
    pre_node = None
    cur_node = head_node

    while cur_node:
        # 如果当前节点与next节点相等 则都删除
        if cur_node.next and cur_node.data == cur_node.next.data:
            next_node = cur_node.next
            # 找到下一个不等的节点
            while next_node.next and next_node.next.data == cur_node.data:
                next_node = next_node.next

            # 前两个节点已删除 故head_node指向第三个节点或者更后面的节点
            if cur_node == head_node:
                # 更新头节点
                head_node = next_node.next
            else:
                pre_node.next = next_node.next

            cur_node = next_node.next
        else:
            # 当前节点与next节点不等
            pre_node = cur_node
            cur_node = cur_node.next

    return head_node



if __name__ == '__main__':

    l = LinkList()
    l.init_list([1 ,2 ,3 ,3 ,4, 4, 5])

    result = delete_repeated_node(l)
    while result:
        print(result.data)
        result = result.next