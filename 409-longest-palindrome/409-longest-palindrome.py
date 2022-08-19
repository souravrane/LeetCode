from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        charCount = defaultdict(int)
        for char in s:
            charCount[char] += 1
        
        isOdd = 0
        palindromeLength = 0
        for char in charCount:
            if charCount[char] % 2:
                palindromeLength += charCount[char] - 1
                isOdd = 1
            else:
                palindromeLength += charCount[char]
        
        return palindromeLength + isOdd
            
    
        
        