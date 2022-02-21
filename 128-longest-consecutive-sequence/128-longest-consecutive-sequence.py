class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        longest = 0
        for n in numSet:
            #  we check for the left value because that marks the start of a new sequence
            if (n - 1) not in numSet:
                count = 0
                # check how many consecutive numbers exist
                while (n + count) in numSet:
                    count += 1
                
                longest = max(longest,count)
        
        return longest
                    
            
            