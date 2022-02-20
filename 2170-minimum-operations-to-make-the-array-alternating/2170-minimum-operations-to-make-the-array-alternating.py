from collections import defaultdict
from functools import cmp_to_key
import math

def compare(a,b):
    if a[1] > b[1]:
        return -1
    return 1

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        odd = defaultdict(int)
        even = defaultdict(int)
                
        for i in range(len(nums)):
            if i % 2 == 0:
                even[nums[i]] += 1 
            else:
                odd[nums[i]] += 1
        
        oc = len(nums) // 2
        ec =  len(nums) - oc
                
        odd_items = sorted(odd.items(), key=cmp_to_key(compare))
        even_items = sorted(even.items(), key=cmp_to_key(compare))

        res = 0
        if odd_items[0][0] == even_items[0][0]:
            maxFreqOdd = odd_items[0][1]
            maxFreqEven = even_items[0][1]
            
            secondMaxFreqOdd, secondMaxFreqEven = 0,0
            if len(odd_items) > 1: secondMaxFreqOdd = odd_items[1][1]
            if len(even_items) > 1: secondMaxFreqEven = even_items[1][1]
            
            res = len(nums) - max(maxFreqOdd + secondMaxFreqEven, maxFreqEven + secondMaxFreqOdd)
            return res
        
        res = len(nums) - (odd_items[0][1] + even_items[0][1])    
        return res
            
                 

'''
1. even positions should be same
2. odd positions should be same

Search for the num in each hashmap with the maximum and second maximum frequencies:
If the two num's with the maximum frequencies are not equal, then return len(nums) - (maxFreqOdd + maxFreqEven);
Otherwise return len(nums) - max(maxFreqOdd + secondMaxFreqEven, maxFreqEven + secondMaxFreqOdd).

'''