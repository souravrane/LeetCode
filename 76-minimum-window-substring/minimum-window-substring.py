from collections import Counter
from functools import reduce

class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if t == "": return ""
        
        result = list()
        need = Counter(t)
        have = defaultdict(int)
        for c in need: have[c] = 0
        lettersUsed = 0
        start = 0

        for end in range(len(s)):
            letter = s[end]

            if letter in need:
                have[letter] += 1
                if have[letter] <= need[letter]: lettersUsed += 1
                
            while lettersUsed == len(t):
                result.append((start, end))
                oldLetter = s[start]
                if oldLetter in need: have[oldLetter] -= 1
                if have[oldLetter] < need[oldLetter]: lettersUsed -= 1
                start += 1
        
        if not result: return ""

        p = reduce(lambda x, y: x if x[1] - x[0] < y[1] - y[0] else y, result)
        return s[p[0] : p[1] + 1]
    
