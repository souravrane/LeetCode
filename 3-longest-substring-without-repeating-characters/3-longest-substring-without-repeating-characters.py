from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        n = len(s)
        
        if n == 0: return 0
        
        longest = 1
        
        h = {}
        for end in range(n):
            char = s[end]
            
            if char in h:
                start = max(start, h[char] + 1)

            longest = max(longest, end - start + 1)
                    
            h[char] = end
        
        return longest

