from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        idCount = {}
        uam = defaultdict(int)
        
        for log in logs:
            Id = log[0]
            time = log[1]
            
            if Id in idCount:
                idCount[Id].add(time)
            else:
                idCount[Id] = set([time])
        
        for key in idCount:
            x = len(idCount[key])
            uam[x] += 1
        
        res = [0]*k
        for key in uam:
            res[key-1] = uam[key]
            
        return res
        