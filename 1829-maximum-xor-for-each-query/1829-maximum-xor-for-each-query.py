class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:        
        # calculate the prefix xor
        prefix_xor = [nums[0]]
        for i in range(1,len(nums)):
            prefix_xor.append(prefix_xor[i-1] ^ nums[i])
                
        res = []
        for i in range(len(nums)-1,-1,-1):
            # given N calculate a number that gives us the maxium possible xor
            max_k = 2**maximumBit - 1
            k = max_k ^ prefix_xor[i]
            res.append(k)
        
        return res
        