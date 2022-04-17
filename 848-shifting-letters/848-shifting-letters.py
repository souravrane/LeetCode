class Solution:
    def shift(self, ch, k):
        newValue = ord('a') + (ord(ch) - ord('a') + k) % 26
        return chr(newValue)
    
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        newS = ['']*n
        
        currShifts = 0
        
        for i in range(n-1,-1,-1):
            currShifts += shifts[i]
            char = s[i]
            newS[i] = self.shift(char, currShifts)
        
        return ''.join(newS)