class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        '''
        for each histogram find the index of nearest smallest histogram to its left
        and index of nearest smallest histogram to its right
        
        Why so ?
        The nearest smallest histograms on left and right show you the boundaries upto which 
        the current histogram can expand. The index gives you the position upto which this expansion can happen
        for example : [2, 1, 5, 6, 2, 3]
        
        - if we consider "1" then the nearest smallest to its left is nothing, so left boundary is at -1
          nearest smallest to its right is nothing, so its right boundary is 6
          so we can say that the max area formed by histogram "1" is (rightIndex - leftIndex - 1) * histogram  = (6 - (-1) -1) * 1 = 6 units
          
         - if we consider "5"
           "index" of nearest smallest histogram to right : 4 
           "index" of nearest smallest histogram to left : 1
           so max area that can be formed is (4 - 1 - 1) * 5 = 10 units
         
         This way we can find out all such possible areas and pick the max out of it.
         
        '''
        
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