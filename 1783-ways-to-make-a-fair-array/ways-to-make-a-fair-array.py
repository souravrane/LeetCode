class Solution:
    def getPrefixArrays(self, nums: List[int]) -> List[List[int]]:
        even, odd = list(), list()
        e, o = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0: e += nums[i]
            else: o += nums[i]
            even.append(e)
            odd.append(o)
        return [even, odd]

    def waysToMakeFair(self, nums: List[int]) -> int:
        pEven, pOdd = self.getPrefixArrays(nums)
        count = 0
    
        for i in range(len(nums)):
            even = pOdd[-1] - pOdd[i]
            odd = pEven[-1] - pEven[i]
            if i != 0:
                even += pEven[i-1]
                odd += pOdd[i-1]
            if even == odd: count += 1
        
        return count