class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        min_abs = float('inf')
        closest_value = 0
        
        for i in range(len(nums)):
            a = nums[i] 
            l = i+1
            r = len(nums)-1
            
            # we begin 2 sum here
            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum == target:
                    return target
                
                # we check for the least absolute difference amongst the tripplets
                difference = abs(target-three_sum)
                if difference < min_abs:
                    closest_value = three_sum
                    min_abs = difference
                    
                if three_sum < target:
                    l += 1
                else:
                    r -= 1
                   
        return closest_value
        
        