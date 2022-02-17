class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = sorted(nums)
        max_seq = 0
        i,j=0,0
        n = len(nums)
        while j < n:
            hd = nums[j]-nums[i]
            
            if hd == 1:
                max_seq = max(max_seq, j - i + 1)
                j += 1                
            elif hd < 1:
                j += 1
            else:
                i += 1
          
        return max_seq
                