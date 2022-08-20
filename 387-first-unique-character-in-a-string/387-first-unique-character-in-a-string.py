class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets = [0]*26
        for char in s:
            alphabets[ord(char) - ord('a')] += 1
        
        for i in range(len(s)):
            char = s[i]
            if alphabets[ord(char) - ord('a')] == 1: return i
        
        return -1
        