from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        n = len(s)
        
        if n == 0: return 0
        
        longest = 1
        
        visited = {}
        for end in range(n):
            char = s[end]
            
            if char in visited:
                start = max(start, visited[char] + 1)

            longest = max(longest, end - start + 1)
                    
            visited[char] = end
        
        return longest

