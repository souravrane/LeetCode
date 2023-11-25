class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                found = True
                for j in range(1, len(needle)):
                    if (i + j) >= len(haystack) or haystack[i+j] != needle[j]:
                        found = False
                        break
                if found: return i
        return -1
        