class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        size = 0
        lookUp = defaultdict(int) 
        for right in range(len(s)):
            letter = s[right]
            print(letter)
            lookUp[letter] += 1
            while lookUp[letter] > 1:
                letter2 = s[left]
                lookUp[letter2] -= 1
                left += 1
            size = max(size, right - left + 1)
        return size
                
        