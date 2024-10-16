class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = list()
        sizeSoFar = 0

        temp = list()
        for i in range(len(words)):
            w = words[i]

            sizeSoFar += len(w)
            temp.append(w)
            print(sizeSoFar, temp)
            
            if sizeSoFar == maxWidth or (i + 1 < len(words) and sizeSoFar + len(words[i + 1]) + 1 > maxWidth):
                print(temp)
                result.append(self.formatString(temp, maxWidth))
                sizeSoFar = 0
                temp.clear()
            else:
                sizeSoFar += 1
        
        if temp: result.append(self.formatString(temp, maxWidth, True))
        return result
    
    def formatString(self, words: List[str], maxWidth: int, isEnd = False) -> str:
        if len(words) == 1:
            return words[0] + (" " * (maxWidth - len(words[0])))
        
        if isEnd:
            text = " ".join(words)
            return text + " " * (maxWidth - len(text))

        result = list()
        totalTextLength = 0
        for w in words: totalTextLength += len(w)

        remainingSpace = maxWidth - totalTextLength
        remainingWords = len(words)
        for w in words:
            result.append(w)
            if remainingSpace > 0:
                space = ceil(remainingSpace / (remainingWords - 1))
                result.append(" " * space)
                remainingSpace -= space
                remainingWords -= 1
        
        return ''.join(result)



        