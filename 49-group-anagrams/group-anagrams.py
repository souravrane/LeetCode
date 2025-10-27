from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in range(len(strs)):
            word = strs[i]
            count = [0] * 26
            for k in word:
                count[ord(k) - ord('a')] += 1
            result[tuple(count)].append(word)
        
        return list(result.values())