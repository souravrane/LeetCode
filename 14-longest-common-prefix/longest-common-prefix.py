class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = []
        firstWord = strs[0]

        for i in range(len(firstWord)):
            char = firstWord[i]
            for j in range(1,len(strs)):
                word = strs[j]
                if i >= len(word) or word[i] != char: 
                    return ''.join(result)
            result.append(char) 
        return ''.join(result)
                
        