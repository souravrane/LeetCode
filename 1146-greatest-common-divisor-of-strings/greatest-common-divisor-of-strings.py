class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = ''
        i, j = 0, 0
        common = []
        
        while(i < len(str1) and j < len(str2)):
            if(str1[i] == str2[j]):
                common.append(str1[i])
                if(len(str1) % len(common) == 0 and len(str2) % len(common) == 0):
                    result = ''.join(common)
                i += 1
                j += 1
            else:
                break
        
        if(str1.count(result)*len(result) == len(str1) and str2.count(result)*len(result) == len(str2)): return result
        return ''
         