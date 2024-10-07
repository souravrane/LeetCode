class RandomizedSet:

    def __init__(self):
        self.cache = dict() #(num, index) pair
        self.nums = list()

    def insert(self, val: int) -> bool:
        if val in self.cache: return False
        self.nums.append(val)
        self.cache[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.cache: return False
        idx = self.cache[val]
        self.nums[idx] = self.nums[-1]
        self.cache[self.nums[-1]] = idx
        del self.cache[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()