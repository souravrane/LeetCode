class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
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