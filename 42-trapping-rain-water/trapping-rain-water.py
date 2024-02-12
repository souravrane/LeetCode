class Solution:
    def trap(self, height: List[int]) -> int:
        maxElevation = max(height)
        maxIndex = height.index(maxElevation)

        water = 0
        leftElevation = 0
        for i in range(maxIndex):
            water += leftElevation - height[i] if leftElevation - height[i] > 0 else 0
            leftElevation = max(leftElevation, height[i])
        
        rightElevation = 0
        for i in range(len(height)-1, maxIndex, -1):
            water += rightElevation - height[i] if rightElevation - height[i] > 0 else 0
            rightElevation = max(rightElevation, height[i])
        
        return water


        