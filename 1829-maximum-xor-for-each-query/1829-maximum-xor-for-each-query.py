class Solution:
    
    # given N calculate a number that gives us the maxium possible xor
    def maximise(self,n,b):
        max_k = (2**b)-1
        return n ^ max_k
        
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:        
        # calculate the prefix xor
        prefix_xor = [nums[0]]
        for i in range(1,len(nums)):
            prefix_xor.append(prefix_xor[i-1] ^ nums[i])
                
        res = []
        for i in range(len(nums)-1,-1,-1):
            k = self.maximise(prefix_xor[i],maximumBit)
            res.append(k)
        
        return res
        