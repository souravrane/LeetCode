class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wordMap = defaultdict(list)
        for i in range(len(strs)):
            originalWord = strs[i]
            word = ''.join(sorted(originalWord))
            wordMap[word].append(originalWord)
        return [x for x in wordMap.values()]

            
        