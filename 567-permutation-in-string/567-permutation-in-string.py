from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        def compareSet(x,y):
            for i in range(26):
                if x[chr(ord('a') + i)] != y[chr(ord('a') + i)]: return False
            return True
        
        s1Set = defaultdict(int)
        charSet = defaultdict(int)
        
        for char in s1: s1Set[char] += 1
        
        for i in range(len(s1)):
            char = s2[i]
            charSet[char] += 1
        
        if compareSet(s1Set, charSet): return True
        
        for i in range(len(s1),len(s2)):
            remove = s2[i-len(s1)]
            add = s2[i]
            charSet[remove] -= 1
            charSet[add] += 1
            if compareSet(s1Set, charSet): return True
        return False
                    
        