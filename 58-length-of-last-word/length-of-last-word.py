class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWordExist = 0
        lastWord = 0
        for i in range(len(s)-1,-1,-1):
            character = s[i]
            if character == " " and lastWordExist == 0: continue
            if character == " " and lastWordExist == 1: break
            lastWord += 1
            lastWordExist = 1
            
        return lastWord
        