class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candy = [1]*n
        
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + candy[i]
        
        print(candy)
        
        for j in range(n-2,-1,-1):
            if ratings[j] > ratings[j+1] and candy[j] <= candy[j+1]:
                candy[j] = candy[j+1] + 1
        
        print(candy)

        return sum(candy)
        
        
        
        '''
        [1,3,2,1]
         1 2 2 1
                 
        '''