class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedChars = set()
        start, maxSize = 0, 0
        for i in range(len(s)):
            c = s[i]
            if c not in visitedChars:
                visitedChars.add(c)
                maxSize = max(maxSize, i - start + 1)
            else:
                while s[start] != c:
                    visitedChars.remove(s[start])
                    start += 1
                start += 1
        return maxSize 
        