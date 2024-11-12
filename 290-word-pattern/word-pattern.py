class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words): return False

        charMap = defaultdict(str)
        index = 0
        for char in pattern:
            if char not in charMap: charMap[char] = words[index]
            elif charMap[char] != words[index]: return False
            index += 1

        wordMap = defaultdict(str)
        index = 0
        for word in words:
            if word not in wordMap: wordMap[word] = pattern[index]
            elif wordMap[word] != pattern[index]: return False
            index += 1
            
        return True

        