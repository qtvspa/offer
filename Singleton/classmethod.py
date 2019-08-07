# -*- coding:utf-8 -*-


""" 用classmethod实现支持多进程的单例模式"""

import threading


class SingleTon(object):

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        with SingleTon._instance_lock:
            if not hasattr(SingleTon, '_instance'):
                SingleTon._instance = SingleTon()
        return SingleTon._instance


if __name__ == '__main__':

    a = SingleTon().instance()
    b = SingleTon().instance()
    print(a)
    print(b)
