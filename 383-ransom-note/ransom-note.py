from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = Counter(ransomNote)
        m_count = Counter(magazine)
        
        for k in r_count.keys():
            if k not in m_count or (r_count[k] > m_count[k]): return False
        
        return True