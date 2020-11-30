""" 使用OrderedDict实现lru

    lru原理：当对key进行访问时时，将该key放到队列的最前端（或最后端），这样就实现了对key按其最后一次访问的时间降序（或升序）排列
            当增加新key时，如果空间满了，删除队尾（或队首）的对象
"""

import collections


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value
