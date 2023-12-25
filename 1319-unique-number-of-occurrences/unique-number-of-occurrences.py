from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freqMap = defaultdict(int)
        for num in arr: freqMap[num] += 1
        return len(freqMap.values()) == len(set(freqMap.values()))
        