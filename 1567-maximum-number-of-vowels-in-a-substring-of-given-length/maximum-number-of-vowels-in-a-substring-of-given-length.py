class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        maxVowels = 0

        for i in range(k):
            if s[i] in vowels:
                maxVowels += 1
        
        count = maxVowels
        for i in range(k,len(s)):
            if s[i-k] in vowels: count -= 1
            if s[i] in vowels: count += 1
            maxVowels = max(maxVowels, count)
        
        return maxVowels

