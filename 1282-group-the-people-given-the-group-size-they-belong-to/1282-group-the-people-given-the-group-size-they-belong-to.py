class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        h = {}
        for i in range(len(groupSizes)):
            group = groupSizes[i]
            if group in h:
                h[group].append(i)
            else:
                h[group] = [i]
        
        res = []    
        for group in h:
            g = h[group]
            for j in range(0,len(g),group):
                res.append(g[j:j+group])
        
        return res
        