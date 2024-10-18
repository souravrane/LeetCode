class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp, rp = 0, len(height) - 1
        maxWater = 0

        while lp < rp:
            maxWater = max(maxWater, min(height[lp], height[rp]) * (rp - lp))
            if height[lp] <= height[rp]: lp += 1
            else: rp -= 1
        
        return maxWater