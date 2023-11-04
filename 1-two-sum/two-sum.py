class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        ind={}
  
        for i in range(len(nums)):
            
            n=nums[i]
            c=target-n
            
            if c in ind:
                return [ind[c],i]
            else:
                ind[n]=i
          

            
            
                
        
       