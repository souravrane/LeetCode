from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        # replace all odd number with 1s and even numbers with 0s
        # this will make the problem find subarrays with sum = k
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
        
        h = defaultdict(int)
        h[0] = 1
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in h:
                count += h[prefix_sum - k]
            
            h[prefix_sum] += 1
                
            
        return count
                

            
                
                
            
            