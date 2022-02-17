class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pf = [0]*10001
        for t in trips:
            passengers = t[0]
            start = t[1]
            end = t[2]
            pf[start] += passengers
            pf[end] -= passengers
            
        for i in range(10001):
            if i == 0 and pf[i] > capacity: return False
            pf[i] += pf[i-1]
            if pf[i] > capacity:
                return False
        
        return True
            
        