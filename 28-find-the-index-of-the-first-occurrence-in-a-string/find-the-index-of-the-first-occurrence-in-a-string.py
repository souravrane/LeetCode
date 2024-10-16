class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            char = haystack[i]
            found = True
            if char == needle[0]:
                for j in range(len(needle)):
                    if i + j >= len(haystack) or needle[j] != haystack[i + j]:
                        found = False
                        break
                if found: return i
        return -1
        