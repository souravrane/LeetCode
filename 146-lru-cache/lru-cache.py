class Node:
    def __init__(self, key, value):
        self.key = key
        self.data = value
        self.next = self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.left, self.right = Node(-1,-1),  Node(-1,-1)
        self.left.next, self.right.prev = self.right, self.left
    
    def get(self, key: int) -> int:
        if key in self.cache:
            # update it to recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].data
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # update it to the recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            self.cache[key].data = value
            return
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        self.size += 1

        if self.size > self.capacity:
            lru = self.right.prev
            self.remove(lru)
            del self.cache[lru.key]
            self.size -= 1
    
    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
    

    def insert(self, node):
        left, right = self.left, self.left.next
        left.next = node
        node.prev = left
        right.prev = node
        node.next = right


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)