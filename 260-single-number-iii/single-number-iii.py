class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums: xor ^= num

        '''
        This mask is to just keep 1 of the all of the set bits active.
        '''
        mask = (xor & (xor - 1)) ^ xor          

        num1, num2 = 0, 0
        for num in nums:
            if num & mask: num1 ^= num
            else: num2 ^= num
        
        return [num1, num2]