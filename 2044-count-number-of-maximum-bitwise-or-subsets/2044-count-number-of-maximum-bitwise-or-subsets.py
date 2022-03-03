

class Solution:
    def __init__(self):
        self.maxOR = 0
        self.dp = [0]
        
    def subsetsOR(self,index,OR,arr):
        if index == len(arr):
            if OR == self.maxOR: return 1
            return 0
        
        if self.dp[index][OR] != -1:
            return self.dp[index][OR]
        
        self.dp[index][OR] = self.subsetsOR(index+1, OR | arr[index],arr ) + self.subsetsOR(index+1, OR,arr )
        return self.dp[index][OR]
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        for num in nums:
            self.maxOR = self.maxOR | num
        
        self.dp = [[-1 for i in range(self.maxOR+1)] for j in range(n+1)]
        return self.subsetsOR(0,0,nums)
        
        
'''
1 2 3 4
[0]
[0] [1]
[0] [1] [2] [2] 
[0] [1] [2] [2] [3] [3] [3] [3]

'''