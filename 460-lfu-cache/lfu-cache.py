from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2val = dict()
        self.key2freq = dict()
        self.freq2key = defaultdict(OrderedDict)
        self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        
        old_freq = self.key2freq[key]
        self.key2freq[key] = old_freq + 1
        self.freq2key[old_freq].pop(key)

        if len(self.freq2key[old_freq]) == 0:
            del self.freq2key[old_freq]

        # add a key : True pair to the ordered dictionary
        self.freq2key[old_freq + 1][key] = True 

        if self.minf not in self.freq2key: self.minf += 1
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        # if key exists update the val and call get.
        if key in self.key2val:
            self.key2val[key] = value
            self.get(key)
            return
        
        # evict
        if len(self.key2val) == self.capacity:
            del_key, _ = self.freq2key[self.minf].popitem(last = False)
            del self.key2freq[del_key]
            del self.key2val[del_key]

        # create new key
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = True
        self.minf = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)