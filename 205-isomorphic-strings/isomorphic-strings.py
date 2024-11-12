class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        charMap = defaultdict(str)
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            if sc not in charMap: charMap[sc] = tc
            elif charMap[sc] != tc: return False

        charMap = defaultdict(str)
        for i in range(len(s)):
            sc, tc = s[i], t[i]
            if tc not in charMap: charMap[tc] = sc
            elif charMap[tc] != sc: return False

        return True 
