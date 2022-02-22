class Solution:
    
    # given N calculate the maxium XOR value it can achieve with a b bit number
    def maximise(self,n,b):
        shift = 0
        res = 0
        while shift < b:
            if n & (1 << shift) == 0:
                res = res | (1 << shift)
            shift += 1
        return res
        
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
        