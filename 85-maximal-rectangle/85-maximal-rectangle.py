class Solution:
    def rectangleInHistogram(self,heights):
        n = len(heights)
        NSL = [0]*n        
        NSR = [0]*n
        
        # find all the indices of nearest smallest element to left
        stack = []
        top = -1
        for i in range(n):
            while top != -1 and heights[stack[top]] >= heights[i]:
                stack.pop()
                top -= 1
            
            if top == -1: NSL[i] = -1
            else: NSL[i] = stack[top]
            
            stack.append(i)
            top += 1
        
        # find all the indices of nearest smallest element to right
        stack = []
        top = -1
        for i in range(n-1,-1,-1):
            while top != -1 and heights[stack[top]] >= heights[i]:
                stack.pop()
                top -= 1
            
            if top == -1: NSR[i] = n
            else: NSR[i] = stack[top]
            
            stack.append(i)
            top += 1

  
        maxArea = 0
        for i in range(n):
            area = (NSR[i] - NSL[i] - 1) * heights[i]
            maxArea = max(maxArea,area)
        
        return maxArea
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        Each row can be thought of as an histogram.
        As we go to the next row, if we find a 1 in the above cell in the current row, we 
        add that up making it a bigger histogram.!
        
        Then solve the problem for that row. 
        If we find a zero then we dont include the zeroes above as the histogram would break
        at that cell.
        
        Tricky question. 
        https://leetcode.com/problems/largest-rectangle-in-histogram/
        The above question is a pre requisite for this question.
        
        '''
        
        rows = len(matrix)
        columns = len(matrix[0])
        maxRectangle = 0
        
        histogramSoFar = [0]*columns
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] != "0": 
                    histogramSoFar[j] += int(matrix[i][j])
                else:
                    histogramSoFar[j] = 0 # if its 0 then we reset the histogram
                    
            rowMaxRectangle = self.rectangleInHistogram(histogramSoFar)
            maxRectangle = max(maxRectangle,rowMaxRectangle)
        
        return maxRectangle
        
        
        
        