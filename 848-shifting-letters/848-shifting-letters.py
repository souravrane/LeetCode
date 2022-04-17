class Solution:
    def shift(self, ch, k):
        newValue = ord('a') + (ord(ch) - ord('a') + k) % 26
        return chr(newValue)
    
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        currShifts = 0
        newS = ''
        for i in range(len(s)-1,-1,-1):
            currShifts += shifts[i]
            char = s[i]
            newS = self.shift(char, currShifts) + newS
        
        return newS