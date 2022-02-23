class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        s = set()
        for i in points:
            s.add(i[0])
        
        s = sorted(list(s))
        
        widest_area = 0
        
        # we just need to check the x axis regions
        for i in range(1,len(s)):
            p2 = s[i]
            p1 = s[i-1]
            widest_area = max(widest_area, p2-p1)
            
        return widest_area