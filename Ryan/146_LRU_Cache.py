# Solution 1 - Normal dict and list as FIFO queue (stupid solution)
# Runtime: 2452 ms, faster than 5.00% of Python3 online submissions for LRU Cache.
# Memory Usage: 73 MB, less than 21.31% of Python3 online submissions for LRU Cache.
class LRUCache:
    def __init__(self, capacity: int):
        self.max_size = capacity
        self.lru = {}
        self.fifo_q = []

    def get(self, key: int) -> int:
        if key in self.lru:
            self.update(key)
            return self.lru[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            self.lru[key] = value
            self.update(key)
        elif len(self.fifo_q) == self.max_size:
            temp = self.fifo_q.pop(0)
            del self.lru[temp]
            self.lru[key] = value
            self.fifo_q.append(key)
        else:
            self.lru[key] = value
            self.fifo_q.append(key)
            
    def update(self, key: int):
        idx = self.fifo_q.index(key)
        temp = self.fifo_q.pop(idx)
        self.fifo_q.append(temp)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Solution 2 - OrderedDict
from collections import OrderedDict
class LRUCache(OrderedDict):  # inherits from object OrderedDict

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)