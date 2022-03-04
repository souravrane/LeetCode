class Solution:
    def __init__(self):
        self.res = [[1],[1,1]]
        
    def generate(self, numRows: int) -> List[List[int]]:
        
        def generateTriangle(arr,rows):
            if rows == 0:
                return
            
            newRow = [1]
            for i in range(1,len(arr)):
                newRow.append(arr[i]+arr[i-1])
            newRow.append(1)
            self.res.append(newRow)
            
            return generateTriangle(newRow,rows-1)
            
        if numRows == 1:
            return self.res[:1]
        
        if numRows == 2:
            return self.res[:2]
        
        generateTriangle([1,1],numRows-2)
        
        return self.res
        
