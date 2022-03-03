maxOR = 0
dp = [0]

class Solution:
    def subsetsOR(self,index,OR,arr):
        if index == len(arr):
            if OR == maxOR: return 1
            return 0
        
        if dp[index][OR] != -1:
            return dp[index][OR]
        
        dp[index][OR] = self.subsetsOR(index+1, OR | arr[index],arr ) + self.subsetsOR(index+1, OR,arr )
        return dp[index][OR]
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        global maxOR
        global dp
        n = len(nums)
        maxOR = 0
        for num in nums:
            maxOR = maxOR | num
        
        dp = [[-1 for i in range(maxOR+1)] for j in range(n+1)]
        return self.subsetsOR(0,0,nums)
        
        
'''
1 2 3 4
[0]
[0] [1]
[0] [1] [2] [2] 
[0] [1] [2] [2] [3] [3] [3] [3]

'''