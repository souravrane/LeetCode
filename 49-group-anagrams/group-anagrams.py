from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for i in range(len(strs)):
            s = strs[i]
            sorted_s = ''.join(sorted(s))
            result[sorted_s].append(s)
        
        return list(result.values())


        