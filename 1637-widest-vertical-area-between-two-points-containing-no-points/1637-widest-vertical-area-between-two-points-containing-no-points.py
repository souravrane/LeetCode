from functools import cmp_to_key
def compare(a,b):
    if a[0] <= b[0]:
        return -1
    return 1

class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(points, key=cmp_to_key(compare))
        widest_area = 0
        
        # we just need to check the x axis regions
        for i in range(1,len(points)):
            p2 = points[i]
            p1 = points[i-1]
            widest_area = max(widest_area, p2[0]-p1[0])
            
        return widest_area