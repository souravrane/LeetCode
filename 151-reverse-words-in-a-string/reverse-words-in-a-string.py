class Solution:
    def reverseWords(self, s: str) -> str:
        wordList = list()
        start = 0
        for i in range(len(s)):
            char = s[i]
            if char == " ":
                word = s[start:i]
                if len(word) > 0: wordList.append(word)
                start = i + 1
        
        if start < len(s):
            wordList.append(s[start:])

        wordList.reverse()
        return ' '.join(wordList)
