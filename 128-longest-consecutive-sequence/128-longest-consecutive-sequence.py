class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        longest = 0
        for n in numSet:
            if (n - 1) not in numSet:
                count = 0
                while (n + count) in numSet:
                    count += 1
                
                longest = max(longest,count)
        
        return longest
                    
            
            