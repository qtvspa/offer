# -*- coding:utf-8 -*-

""" 基于__new__()方法实现单例模式 """


import threading


class SingleTon(object):

    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with SingleTon._instance_lock:
                cls._instance = super(SingleTon, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':

    a = SingleTon()
    b = SingleTon()
    print(a)
    print(b)
