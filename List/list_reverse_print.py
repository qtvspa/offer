# -*- coding:utf-8 -*-


""" 从尾到头打印链表
    通常，这种情况下，我们不希望修改原链表的结构。
    返回一个反序的链表，这就是经典的“后进先出”，我们可以使用栈实现这种顺序。
    每经过一个结点的时候，把该结点放到一个栈中。当遍历完整个链表后，再从栈顶开始逐个输出结点的值，
    给一个新的链表结构，这样链表就实现了反转。"""

""" 对于python，可以直接使用列表的插入方法，每次插入数据只插入在首位"""


from LIST.linklist_base import LinkList


def print_list_tail2head(LinkList):

    result = []
    p = LinkList.head
    while p:
        result.insert(0, p.data)
        p = p.next
    return result


if __name__ == '__main__':

    node = LinkList()
    node.init_list([1, 4, 7, 9])
    print(print_list_tail2head(node))