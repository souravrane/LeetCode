class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = table[s[-1]]
        for i in range(len(s)-2,-1,-1):
            if table[s[i]] < table[s[i+1]]:
                ans -= table[s[i]]
            else: ans += table[s[i]]
        return ans