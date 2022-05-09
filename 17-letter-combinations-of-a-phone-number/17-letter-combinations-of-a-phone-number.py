class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z'],
        }
        
        if digits == "": return []
        
        res = h[digits[0]]
        
        for i in range(1, len(digits)):
            charList = h[digits[i]]
            
            temp = []
            for char in charList:
                for j in range(len(res)):
                    temp.append(res[j] + char)
            
            res = temp
        
        return res