from collections import defaultdict

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans = 0
        m = 1000000007
        
        count = [0]*101
        for num in arr: count[num] += 1
             
        for i in range(101):
            for j in range(i,101):
                k = target - i - j
                
                if k < 0 or k > 100: continue
                
                if i == j and j == k :
                    ans = ans + count[i]*(count[i]-1)*(count[i]-2) // 6
                    
                elif i == j and j != k:
                    ans = ans + count[i]*(count[i]-1)*count[k] // 2
                
                elif i < j and j < k:
                    ans = ans + count[i]*count[j]*count[k]
                
                ans = ans % m

        return ans