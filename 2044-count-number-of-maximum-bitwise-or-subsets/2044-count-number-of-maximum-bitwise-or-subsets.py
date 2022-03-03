maxOR = 0

class Solution:
    def subsetsOR(self,index,OR,arr):
        if index == len(arr):
            if OR == maxOR: return 1
            return 0
        return self.subsetsOR(index+1, OR | arr[index],arr ) + self.subsetsOR(index+1, OR,arr )
            
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        global maxOR
        maxOR = 0
        for num in nums:
            maxOR = maxOR | num
        return self.subsetsOR(0,0,nums)
        
        
'''
1 2 3 4
[0]
[0] [1]
[0] [1] [2] [2] 
[0] [1] [2] [2] [3] [3] [3] [3]

'''