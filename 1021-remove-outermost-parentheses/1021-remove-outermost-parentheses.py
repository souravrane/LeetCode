class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        counter = 1
        newS = ""
        i = 1
        while i < len(s):
            c = s[i]
            if s[i] == "(":
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                i += 1
                counter = 1
            else:
                newS += c               
            i+=1
           
        return newS
                    
