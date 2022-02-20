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
        
        maxFreqOdd,secondMaxFreqOdd = 0,0
        maxFreqEven,secondMaxFreqEven = 0,0
        odd_element = 0
        even_element = 0
        
        for i in odd:
            if odd[i] > maxFreqOdd:
                maxFreqOdd = odd[i]
                odd_element = i
                
        for i in even:
            if even[i] > maxFreqEven:
                maxFreqEven = even[i]
                even_element = i
                
        del odd[odd_element]
        del even[even_element]
        
        for i in odd:
            if odd[i] > secondMaxFreqOdd:
                secondMaxFreqOdd = odd[i]
                
        for i in even:
            if even[i] > secondMaxFreqEven:
                secondMaxFreqEven = even[i]
                
        res = 0
        if odd_element == even_element:
            res = len(nums) - max(maxFreqOdd + secondMaxFreqEven, maxFreqEven + secondMaxFreqOdd)
        else:
            res = len(nums) - (maxFreqOdd + maxFreqEven)    
        return res
            
                 

'''
1. even positions should be same
2. odd positions should be same

Search for the num in each hashmap with the maximum and second maximum frequencies:
If the two num's with the maximum frequencies are not equal, then return len(nums) - (maxFreqOdd + maxFreqEven);
Otherwise return len(nums) - max(maxFreqOdd + secondMaxFreqEven, maxFreqEven + secondMaxFreqOdd).

'''