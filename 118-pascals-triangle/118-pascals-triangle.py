class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pTriangle = [[1],[1,1]]
        for i in range(3,numRows+1):
            row = [1]
            last = pTriangle[-1]
            for i in range(len(last)-1):
                row.append(last[i] + last[i+1])
            row.append(1)
            pTriangle.append(row)
        
        return pTriangle[:numRows]
            