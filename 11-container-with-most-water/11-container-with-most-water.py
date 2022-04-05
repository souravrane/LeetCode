class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        maxWater = 0
        
        while i < j:
            
            water = min(height[i],height[j]) * (j-i)
            maxWater = max(water, maxWater)
            
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        
        return maxWater