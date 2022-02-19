class Solution:
    def trap(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        leftMax,rightMax = 0,0
        totalWater = 0
        
        while(left<right):
            if height[left] <= height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    totalWater+=leftMax-height[left]
                left+=1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    totalWater+=rightMax-height[right]
                right-=1
                
        return totalWater
        
            
            
        
        
        
        
        
'''

   [0,1,0,2,1,0,1,*3*,2,1,2,1]
sm [3,3,3,3,3,3,3,3,  2,2,2,1]
w  [0,0,1,0,1,2,1,0,0,1,0,0] 6


    [4,2,0,3,2,5]
pm  [4,4,4,4,4,5]
sm  [5,5,5,5,5,5]
w   [0,2,4,1,2,0] 9
'''