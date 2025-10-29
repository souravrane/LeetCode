class Node:
    __slots__ = ("key", "val", "freq", "prev", "next")
    def __init__(self, key: int, val: int, freq: int = 1):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = None
        self.next = None

class DLinkedList:
    """LRU list for a given frequency: head = MRU, tail = LRU."""
    def __init__(self):
        self.head = Node(0, 0)   # sentinel head
        self.tail = Node(0, 0)   # sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def _insert_after(self, prev_node: Node, node: Node):
        node.prev = prev_node
        node.next = prev_node.next
        prev_node.next.prev = node
        prev_node.next = node
        self.size += 1

    def add_to_head(self, node: Node):
        self._insert_after(self.head, node)

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1

    def pop_lru(self) -> Node:
        """Remove and return LRU (node before tail). Assumes non-empty."""
        lru = self.tail.prev
        self.remove(lru)
        return lru

    def is_empty(self) -> bool:
        return self.size == 0

class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.min_freq = 0
        self.key2node = {}               # key -> Node
        self.freq2dll = {}               # freq -> DLinkedList

    def _get_list(self, freq: int) -> DLinkedList:
        if freq not in self.freq2dll:
            self.freq2dll[freq] = DLinkedList()
        return self.freq2dll[freq]

    def _bump(self, node: Node):
        """Move node from freq f to f+1, maintaining LRU within buckets."""
        f = node.freq
        self.freq2dll[f].remove(node)
        if f == self.min_freq and self.freq2dll[f].is_empty():
            self.min_freq += 1
        node.freq = f + 1
        self._get_list(node.freq).add_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key2node or self.cap == 0:
            return -1
        node = self.key2node[key]
        self._bump(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key2node:
            node = self.key2node[key]
            node.val = value
            self._bump(node)
            return

        # Evict if full
        if self.size == self.cap:
            l = self._get_list(self.min_freq)
            evicted = l.pop_lru()               # LRU among least freq
            del self.key2node[evicted.key]
            self.size -= 1

        # Insert new key with freq=1 (MRU in freq=1)
        node = Node(key, value, 1)
        self.key2node[key] = node
        self._get_list(1).add_to_head(node)
        self.min_freq = 1
        self.size += 1
