from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freqMagzine = Counter(magazine)
        freqRansom = Counter(ransomNote)
        for letter in freqRansom:
            if freqMagzine[letter] < freqRansom[letter]: return False
        return True      