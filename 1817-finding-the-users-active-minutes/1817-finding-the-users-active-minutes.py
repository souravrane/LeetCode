from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        uam = {}
        
        for log in logs:
            Id = log[0]
            time = log[1]
            
            if Id in uam:
                uam[Id].add(time)
            else:
                uam[Id] = set([time])
                
        res = [0]*k
        for key in uam:
            x = len(uam[key])
            res[x-1] += 1
        
    
        return res
        