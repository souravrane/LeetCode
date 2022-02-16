class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        if n < 4:
            return []

        res = []
        for i in range(n):
            a = nums[i]
            
            if (i == 0) or nums[i] != nums[i-1]:
                # Three sum
                for j in range(i+1,n):
                    b = nums[j]
                    
                    if (j == i+1) or nums[j] != nums[j-1]:
                        # two sum
                        l = j+1
                        r = n-1
                        while l < r:
                            four_sum = a + b + nums[l] + nums[r]

                            if four_sum > target:
                                r -= 1
                            elif four_sum < target:
                                l += 1
                            else:
                                res.append([a,b,nums[l],nums[r]])
                                l += 1
                                while l < r and nums[l] == nums[l-1]:
                                    l += 1
        return res
                            
            
        
  