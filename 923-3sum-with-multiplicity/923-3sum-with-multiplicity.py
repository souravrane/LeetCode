from collections import defaultdict

class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        '''
        In this problem we look for 3 such triplets which satisfy the below conditions
        
        1) a == b == c
            In this case our ans would be nC3 , where n is total frequency of a,b,c
        
        2) a == b != c
            In this case our ans would be nC2 * frequency(c) where n is the frequency of a and b
        
        3) a != b != c
            In this case our ans would be frequency(a) * frequency(b) * frequency(c)
            
        
        The constraint 0 <= arr[i] <= 100 makes the problem easier for us.
            
        '''

        m = (int)(10**9 + 7)
        ans = 0
        
        freq = [0]*101
        for num in arr: freq[num] += 1
        
        for a in range(101):
            for b in range(a,101):
                c = target - a - b
                
                if c < 0 or c > 100: continue
                
                if a == b and b == c:
                    ans += (freq[a] * (freq[a]-1) * (freq[a]-2)) // 6 
                    
                elif a == b and b != c:
                    ans += (freq[a] * (freq[a]-1) * (freq[c])) // 2
                    
                elif a < b and b < c:
                    ans += freq[a] * freq[b] * freq[c]
                
                ans = ans % m
        
        return ans

                
                