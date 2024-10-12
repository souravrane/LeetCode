class Solution:
    def trap(self, height: List[int]) -> int:
        tallestBuilding = max(height)
        tallestPosition = height.index(tallestBuilding)

        water = 0
        leftTall = 0
        for i in range(tallestPosition):
            water += max(0, leftTall - height[i])
            leftTall = max(leftTall, height[i])
        
        rightTall = 0
        for i in range(len(height)-1, tallestPosition, -1):
            water += max(0, rightTall - height[i])
            rightTall = max(rightTall, height[i])

        return water 