from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        
        ans = 0
        oddFlag = False
        for num in counter.values():
            if num % 2:
                ans += num - 1
                oddFlag = True
            else:
                ans += num
                
        if oddFlag: return ans + 1
        return ans
        
        