
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()

        st = 0
        ans = 0
        
        for e in range(len(s)):
            char = s[e]
            while char in charSet:
                charSet.remove(s[st])
                st += 1
            
            charSet.add(char)
            ans = max(ans, len(charSet)) 
               
        
        return ans