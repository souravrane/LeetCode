class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        title = columnTitle[::-1]
        number = 0
        for i in range(len(title)):
            number += (26**i)*(ord(title[i])-65+1)
        return number