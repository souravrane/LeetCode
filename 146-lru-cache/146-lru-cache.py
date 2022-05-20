class Node:
	def __init__(s, key, value):
		s.key = key
		s.value = value
		s.next = None
		s.prev = None

class LRUCache:
	def __init__(self, capacity: int):
		self.mostRecent = Node(-1, -1)
		self.leastRecent = Node(-1, -1)
		self.mostRecent.next = self.leastRecent
		self.leastRecent.prev = self.mostRecent
		self.hash = {}
		self.size = capacity

    
	def get(self, key: int) -> int:
		if key not in self.hash:
			return -1
		node = self.hash[key]
		self.delete(node)
		self.insert(node)
		return node.value

	def put(self, key: int, value: int) -> None:
		if key in self.hash:
			node = self.hash[key]
			self.delete(node)
		if self.size == len(self.hash):
			self.delete(self.leastRecent.prev)
		self.insert(Node(key, value))

	def insert(self, node):
		self.mostRecent.next.prev = node
		node.next = self.mostRecent.next
		self.mostRecent.next = node
		node.prev = self.mostRecent
		self.hash[node.key] = node

	def delete(self, node):
		self.hash.pop(node.key)
		node.next.prev = node.prev
		node.prev.next = node.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)