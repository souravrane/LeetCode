from functools import cmp_to_key

def compare(a,b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    if int(ab) < int(ba):
        return -1
    return 1


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > -10 and num < 10: return num
        
        nums = []
        sign = -1 if num < 0 else 1
        num = abs(num)
        
        while num > 0:
            nums.append(num % 10)
            num = num // 10
        
        res = ''
        nums = sorted(nums, key=cmp_to_key(compare))
        
        
        # We find the smallest number that can be formed  
        if sign == 1:
            i,zero_count = 0,0
            
            # count the zeroes in the number
            while nums[i] == 0:
                zero_count += 1
                i += 1
                
            res += str(nums[i]) + "0"*zero_count
            
            for j in range(i+1,len(nums)):
                res += str(nums[j])
                
        else: 
            # We find the largest number that can be formed
            for j in range(len(nums)):
                res = str(nums[j]) + res        
            
        
        return sign*int(res)
    
    
    
                
        