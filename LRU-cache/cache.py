from collections import OrderedDict
 
class LRUCache: 
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
 
    def get(self, key: int) -> str:
        if key not in self.cache:
            return ''
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
 
    def set(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
    
    def rem(self, key: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache.popitem()
