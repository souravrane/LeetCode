class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 0
        indexSet = {0}
        
        for i in range(len(s)):
            c = s[i]
            if s[i] == "(":
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                indexSet.add(i)
                indexSet.add(i+1)
                
        newS = ""
        for i in range(len(s)):
            if i not in indexSet:
                newS += s[i]
                
                
        return newS
                    
       