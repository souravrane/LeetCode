class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ['']*(len(word1) + len(word2))
        start = 0
        i,j = 0,0
        while(i < len(word1) and j < len(word2)):
            if(start % 2):
                result[start] = word2[j]
                j += 1
            else:
                result[start] = word1[i]
                i += 1

            start += 1
        
        while(i < len(word1)):
            result[start] = word1[i]
            start += 1
            i += 1
        
        while(j < len(word2)):
            result[start] = word2[j]
            start += 1
            j += 1

        return ''.join(result)