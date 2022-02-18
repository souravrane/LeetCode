class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        def multiply(arr):
            res = 1
            for i in arr: res *= i
            return res
        
        
        if len(nums) == 3: 
            return nums[0]*nums[1]*nums[2]
        
        positive = []
        negative = []
        for i in nums:
            if i >= 0:
                positive.append(i)
            else:
                negative.append(i)
        
        positive = sorted(positive,reverse = True)
        negative = sorted(negative)
        
        p_len = len(positive)
        n_len = len(negative)
        max_product = float(-inf)
        
        if p_len > 2:
            value = multiply(positive[:3])
            max_product = max(max_product,value)
        
        if p_len > 1 and n_len > 0:
            value = multiply(positive[:2]) * negative[-1]
            max_product = max(max_product,value)
        
        if p_len > 0 and n_len > 1:
            value = positive[0] * multiply(negative[:2])
            max_product = max(max_product,value)
            
        if n_len > 2:
            value = multiply(negative[-3:])
            max_product = max(max_product,value)

        
        return max_product
        
        