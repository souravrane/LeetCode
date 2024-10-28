from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = list()
        size = len(words[0])
        freq = Counter(words)
        

        for i in range(size):
            left = i
            window = defaultdict(int)
            wordsUsed = 0

            for right in range(i, len(s) - size + 1, size):
                matched = True
                curFreq = freq.copy()

                w = s[right : right + size]
                if w not in freq:
                    left = right + size
                    window = defaultdict(int)
                    wordsUsed = 0
                    continue

                wordsUsed += 1
                window[w] += 1

                while window[w] > freq[w]:
                    prevW = s[left : left + size]
                    window[prevW] -= 1
                    left += size
                    wordsUsed -= 1
                
                if wordsUsed == len(words): result.append(left)
                
        return result
        