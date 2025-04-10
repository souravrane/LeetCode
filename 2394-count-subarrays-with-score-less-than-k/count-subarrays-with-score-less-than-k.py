class Solution:
    def countSubarrays(self, nums: List[int], score: int) -> int:
        result, curScore = 0, 0
        i = 0
        for j in range(len(nums)):
            curScore += nums[j]
            
            while curScore * (j - i + 1) >= score:
                curScore -= nums[i]
                i += 1
            
            result += j - i + 1
        
        return result

            

