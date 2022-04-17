class Solution:
    def getPalindrome(self,s,i,j):
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            i -= 1
            j += 1
        
        return s[i+1:j]
        
    def longestPalindrome(self, s: str) -> str:
        longestPalin = s[0]
        lengthLongest = 1
        
        for i in range(1,len(s)):
            s1 = self.getPalindrome(s,i-1,i+1)
            s2 = self.getPalindrome(s,i-1,i)
            
            if len(s1) > lengthLongest :
                lengthLongest = len(s1)
                longestPalin = s1
            
            if len(s2) > lengthLongest:
                lengthLongest = len(s2)
                longestPalin = s2
            
        return longestPalin