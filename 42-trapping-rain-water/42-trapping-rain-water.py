class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = 0
        right_wall = height.index(max(height))
        water = 0
        
        # water level in the left half
        for i in range(len(height)):
            if i == right_wall: break
            prefix_max = max(prefix_max,height[i])
            water += prefix_max - height[i]
        
        # water level in the right half
        suffix_max = 0
        for i in range(len(height)-1,-1,-1):
            if i == right_wall: break
            suffix_max = max(suffix_max,height[i])
            water += suffix_max - height[i]

        
        return water
        
            
            
        
        
        
        
        
'''

   [0,1,0,2,1,0,1,*3*,2,1,2,1]
sm [3,3,3,3,3,3,3,3,  2,2,2,1]
w  [0,0,1,0,1,2,1,0,0,1,0,0] 6


    [4,2,0,3,2,5]
pm  [4,4,4,4,4,5]
sm  [5,5,5,5,5,5]
w   [0,2,4,1,2,0] 9
'''