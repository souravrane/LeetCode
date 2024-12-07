class Solution:
    def isMatchingBracket(self, result, bracket):
        if result and (bracket == ")" and result[-1] == "(" or bracket == "]" and result[-1] == "[" or bracket == "}" and result[-1] == "{"):
            return True
        return False

    def isValid(self, s: str) -> bool:
        result = list()
        for bracket in s:
            if bracket in "({[": result.append(bracket)
            else: 
                if self.isMatchingBracket(result, bracket): result.pop()
                else: return False
        
        return len(result) == 0
        