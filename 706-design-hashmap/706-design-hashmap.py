class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        
class MyHashMap:

    def __init__(self):
        self.size = 1007
        self.arr = [None]*self.size
    
    def hashcode(self, key):
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        h = self.hashcode(key)
        newNode = ListNode(key,value)
        
        curr = self.arr[h]

        if curr == None:
            self.arr[h] = newNode
            return
        
        while True:
            if curr.key == key:
                curr.val = value
                return
            
            if curr.next == None: break
            curr = curr.next
        
        curr.next = newNode
        
    def get(self, key: int) -> int:
        h = self.hashcode(key)
        curr = self.arr[h]
        
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        h = self.hashcode(key)
        prev = curr = self.arr[h]
        
        if curr:
            if curr.key == key:
                self.arr[h] = curr.next
                return
            
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    return

                prev = curr
                curr = curr.next        



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)