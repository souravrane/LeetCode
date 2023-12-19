class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        leftMin = [nums[0]]*len(nums)
        rightMax = [nums[-1]]*len(nums)

        for i in range(1,len(nums)):
            leftMin[i] = min(leftMin[i-1], nums[i])
        
        for j in range(len(nums)-2, -1, -1):
            rightMax[j] = max(rightMax[j+1], nums[j])

        for i in range(1, len(nums)-1):
            if(leftMin[i-1] < nums[i] and nums[i] < rightMax[i+1]): return True
        return False

        