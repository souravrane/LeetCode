class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        ans = list()
        for row in range(numRows):
            hop = row
            down = True
            while hop < len(s):
                ans.append(s[hop])
                if row == 0 or row == numRows-1:
                    hop += 2*(numRows-1)
                    continue

                if down:
                    hop += 2*(numRows-1-row)
                else:
                    hop += 2*(row)
                down = not(down)

        return ''.join(ans)