# -*- coding:utf-8 -*-


class ListNode(object):
    # 链表节点类

    # p即模拟所存放的下一个结点的地址, 为了方便传参, 设置p的默认值为None
    def __init__(self, data, p=None):
        self.data = data
        self.next = p


class LinkList(object):
    # 链表类
    def __init__(self):
        self.head = None

    # 链表初始化函数
    def init_list(self, data):
        # 创建头结点
        if len(data) > 0:
            self.head = ListNode(data[0])
            p = self.head
            # 逐个为 data 内的数据创建结点, 建立链表
            for i in data[1:]:
                node = ListNode(i)
                p.next = node
                p = p.next
        else:
            self.head = None

    # 链表判断是否为空
    def is_empty(self):
        if self.head.next == 0:
            print("Empty List!")
            return True
        else:
            return False

    # 链表长度
    def get_length(self):
        if self.is_empty():
            exit(0)
        p = self.head
        l = 0
        while p:
            l += 1
            p = p.next
        return l

    # 遍历链表
    def travel_list(self):
        if self.is_empty():
            exit(0)
        p = self.head
        while p:
            print(p.data)
            p = p.next

    # 插入数据
    def insert_elem(self, key, index):
        if self.is_empty():
            exit(0)
        if index < 0 or index > self.get_length() - 1:
            exit(0)

        pre = None
        p = self.head
        i = 0
        while i <= index:
            pre = p
            p = p.next
            i += 1

        #遍历找到索引值为 index 的结点后, 在其后面插入结点
        node = ListNode(key)
        pre.next = node
        node.next = p

    # 删除数据
    def delete_elem(self, index):

        if self.is_empty():
            exit(0)
        if index < 0 or index > self.get_length()-1:
            exit(0)

        i = 0
        p = self.head
        pre = None
        # 遍历找到索引值为index的结点
        while p.next:
            pre = p
            p = p.next
            i += 1
            if i == index:
                pre.next = p.next
                return True

        # p的下一个结点为空说明到了最后一个结点, 删除之即可
        pre.next = None
