from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = defaultdict(int)
        
        for i in magazine:
            h[i] += 1
        
        for j in ransomNote:
            if j not in h or h[j] == 0: return False
            h[j] -= 1
        
        return True
        