from collections import defaultdict

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        1. length and characters should be same - else No
        2. character count is same  - Yes
        3. frequency count is same - Yes
        4. No if none of the above
        '''
        if len(word1) != len(word2): return False
        
        f1 = defaultdict(int)
        f2 = defaultdict(int)
        for letter in word1: f1[letter] += 1
        for letter in word2: f2[letter] += 1
        for letter in word1:
            if letter not in f2: return False
        
        flag = 1
        for letter in word1:
            if f1[letter] != f2[letter]:
                flag = 0
                break
        if flag: return True

        valueMap1 = defaultdict(int)
        valueMap2 = defaultdict(int)
        for num in f1.values(): valueMap1[num] += 1
        for num in f2.values(): valueMap2[num] += 1
        for num in f1.values():
            if valueMap2[num] != valueMap1[num]: return False
        return True




