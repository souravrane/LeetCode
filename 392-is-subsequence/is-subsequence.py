class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ps = 0
        for i in range(len(t)):
            letter = t[i]
            if ps < len(s) and letter == s[ps]: ps += 1
        return ps == len(s)
        