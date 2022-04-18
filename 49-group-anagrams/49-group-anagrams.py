from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedWords = [ "".join(sorted(s)) for s in strs]
        
        h = defaultdict(list)
        for i in range(len(sortedWords)):
            word = sortedWords[i]
            h[word].append(strs[i])
        
        return h.values()
            
        
        