# -*- coding:utf-8 -*-

""" 定义栈的数据结构，请在类型中实现一个能够得到栈最小元素的min函数。"""

""" 思路
    定义一个辅助栈min用于存放最小元素
"""


class Stack(object):

    def __init__(self):
        self.data = []
        self.min = []

    def push(self, num):
        if not self.data and not self.min:
            self.data.append(num)
            self.min.append(num)
        else:
            self.data.append(num)
            if num < self.min_num():
                self.min.pop()
                self.min.append(num)

    def pop(self):
        return self.data.pop()


    def min_num(self):
        if self.min:
            return self.min[0]
        else:
            return 0


if __name__ == '__main__':
    obj = Stack()

    obj.push(3)
    obj.push(4)
    obj.push(1)
    obj.push(5)
    obj.push(2)

    print(obj.min_num())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
    # print(obj.pop())
