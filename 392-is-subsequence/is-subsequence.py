class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for i in range(len(t)):
            if start < len(s) and t[i] == s[start]:
                start += 1
        return start == len(s)

        