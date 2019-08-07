# -*- coding:utf-8 -*-


""" 装饰器实现单例模式 """


def singleton(cls):

    _instance = {}

    def _single(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _single


@singleton
class S(object):

    def __init__(self, x):
        self.x = x


if __name__ == '__main__':

    a = S(1)
    b = S(2)
    print(a)
    print(b)

