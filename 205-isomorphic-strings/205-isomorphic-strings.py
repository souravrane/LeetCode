class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        isoMap = {}
        n = len(s)
        
        for i in range(n):
            char = s[i]
            if char in isoMap and t[i] != isoMap[char]: return False
            isoMap[char] = t[i]
        
        
        isoMap.clear()
        for i in range(n):
            char = t[i]
            if char in isoMap and s[i] != isoMap[char]: return False
            isoMap[char] = s[i]
        
        return True
        
        
        
        