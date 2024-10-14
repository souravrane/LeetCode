class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = list()
        firstWord = strs[0]

        for i in range(len(firstWord)):
            for word in strs:
                if i == len(word) or firstWord[i] != word[i]: return ''.join(ans)
            ans.append(firstWord[i])
        
        return ''.join(ans)
        