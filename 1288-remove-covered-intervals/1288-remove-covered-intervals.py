from functools import cmp_to_key

def compare(a,b):
    if a[0] < b[0]:
        return -1   
    return 1

class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=cmp_to_key(compare))
        left,right = intervals[0]
        count = 0
        length = 1
        for i in range(1,len(intervals)):
            length += 1
            curr = intervals[i]
            if curr[0] >= left and curr[1] <= right:
                count += 1
            elif curr[0] == left and curr[1] > right:
                count += 1
                right = max(right,curr[1])
            else:
                left = curr[0]
                right = max(right,curr[1])
            
        return length - count

                
                
                
                
                