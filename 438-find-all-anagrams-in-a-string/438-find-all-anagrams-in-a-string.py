from collections import defaultdict

class Solution:
    def isAnagram(self, sCount, pCount):
        for char in sCount:
            if pCount[char] != sCount[char]: return False
        return True
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s): return []
        
        sCount = defaultdict(int)
        pCount = defaultdict(int)
        res = []
        
        for char in p: pCount[char] += 1
        for i in range(len(p)):
            char = s[i]
            sCount[char] += 1
        
        if self.isAnagram(sCount, pCount): res.append(0)
        
        for i in range(1,len(s)-len(p)+1):
            removeChar = s[i-1]
            addChar = s[i + len(p) - 1]
            sCount[removeChar] -= 1
            sCount[addChar] += 1
            if self.isAnagram(sCount, pCount): res.append(i)
        
        return res
            
            