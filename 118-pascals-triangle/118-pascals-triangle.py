class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        def generateTriangle(arr,rows,res):
            if rows == 0:
                return res
            
            newRow = [1]
            for i in range(1,len(arr)):
                newRow.append(arr[i]+arr[i-1])
            newRow.append(1)
            res.append(newRow)
            
            return generateTriangle(newRow,rows-1,res)
            
        res = [[1],[1,1]]
        if numRows == 1:
            return res[:1]
        
        if numRows == 2:
            return res[:2]
        
        return generateTriangle([1,1],numRows-2,res)
        
