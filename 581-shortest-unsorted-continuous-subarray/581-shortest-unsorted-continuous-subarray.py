class Solution:
    def isNotSorted(self, index, num, arr):
        if index == 0:
            return num > arr[index + 1]
        if index == len(arr)-1:
            return num < arr[index - 1]
        return (num < arr[index - 1]) or (num > arr[index + 1])
    
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        '''
        Mark the elements as sorted or unsorted
        using the min and max from the unsorted elements find the left and right index
        
        '''
        minVal = float('inf')
        maxVal = float('-inf')
        
        n = len(nums)
        
        if n == 1: return 0
        
        for i in range(n):     
            curr = nums[i]
            
            if self.isNotSorted(i, curr, nums):
                minVal = min(minVal, curr)
                maxVal = max(maxVal, curr)  

        
        if minVal == float('inf'): return 0
        
        leftIdx = 0
        for i in range(n):
            if nums[i] > minVal:
                leftIdx = i
                break
        
        rightIdx = n-1
        for j in range(n-1,-1,-1):
            if nums[j] < maxVal:
                rightIdx = j
                break
        
        return rightIdx - leftIdx  + 1
        
        
        