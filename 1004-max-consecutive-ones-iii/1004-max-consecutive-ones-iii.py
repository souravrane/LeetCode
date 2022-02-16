class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        n = len(nums)
        max_distance = 0
        
        i,j = 0,0
        zero_count = 0
        
        # The idea is to have a sliding window which always has atmost k zeroes inside it
        while j < n:
            
            if nums[j] == 0:
                zero_count += 1
            
            # if the number of zeroes exceed k inside our window 
            # we start reducing the window to the point where only k zeroes are present.
            
            # if zero_count > k: # redundant condition
            
            while zero_count > k:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1

            if zero_count <= k:
                # now our window has k zeroes we find the distance
                window_size = j-i+1
                max_distance = max(max_distance, window_size)
            
            j += 1
                

        return max_distance
            
            
            
            
          
                        
                
            
        
                        
                
                
                
                    
        
        