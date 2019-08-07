# -*- coding:utf-8 -*-


""" 用元类实现单例模式 """


class Singleton(type):

    def __init__(cls, *args, **kwargs):
        cls.__instance = None
        super().__init__(*args, **kwargs)

    # __call__ 是对于类实例有效，比如说Spam类，是type类的实例
    def __call__(cls, *args, **kwargs):
        print('Singleton __call__ running')
        if not cls.__instance:
            '''
            元类定义__call__方法，可以抢在类运行 __new__ 和 __init__ 之前执行，
            也就是创建单例模式的前提，在类实例化前拦截掉。
            type的__call__实际上是调用了type的__new__和__init__
            '''
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance


class Spam(metaclass=Singleton):

    def __new__(cls):
        print('Spam __new__ running')
        return super().__new__(cls)

    def __init__(self):
        print('Spam __init__ running')


if __name__ == '__main__':

    a = Spam()
    b = Spam()
    print(a is b)
