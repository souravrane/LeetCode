class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums = [2,7,11,15], target = 9
        h = {2:0,..}
        check for target - nums[i]
        
        '''
        
        h = {}
        for i in range(len(nums)):
            if target - nums[i] in h:
                return [h[target - nums[i]],i]
            h[nums[i]] = i
        
    