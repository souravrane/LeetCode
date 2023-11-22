class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            distanceToGoal = goal - i
            if nums[i] >= distanceToGoal :
                goal = i
        return True if goal == 0 else False
            
        