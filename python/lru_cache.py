# LRU Cache
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4

#using collections 

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key) 
            return self.cache[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) >= self.size:
                self.cache.popitem(last=False) #LIFO
        else:
            self.cache.move_to_end(key)
        self.cache[key] = value

# creating a doubly linked list from scratch

class LRUCache2:
    def __init__(self, capacity):
        self.cache = {}
        self.size = capacity or 1
        self.current = 0
        self.recent_list = DLL()

    def insert(self, key, value):
        if key not in self.cache:
            if self.current == self.size:
                self.remove_least_recent()
            else:
                self.current += 1
            self.cache[key] = DLLNode(key, value)
        else:
            self.replace_key(key, value)
        self.update(self.cache[key])

    def get_value(self, key):
        if key not in self.cache:
            return -1
        self.update(self.cache[key])
        return self.cache[key].value

    def get_key(self):
        return self.recent_list.head.key

    def remove_least_recent(self):
        key = self.recent_list.tail.key
        self.recent_list.remove_tail()
        del self.cache[key]

    def update(self, node):
        self.recent_list.set_head(node)

    def replace_key(self, key, value):
        if key not in self.cache:
            return -1
        self.cache[key].value = value


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def set_head(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bind()
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_bind(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

