class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabets = [0]*26
        
        for char in magazine:
            alphabets[ord(char) - ord('a')] += 1
        
        for char in ransomNote:
            index = ord(char) - ord('a')
            if alphabets[index] == 0: return False
            alphabets[index] -= 1
        
        return True
        