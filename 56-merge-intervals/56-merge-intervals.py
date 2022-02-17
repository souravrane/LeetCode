from functools import cmp_to_key

class Solution:
    def compare(self,a,b):
        if a[0] < b[0]:
            return -1
        
        if a[0] > b[0]:
            return 1
        
        if a[1] < b[1]:
            return -1
        else:
            return 1
        
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=cmp_to_key(self.compare))
        print(intervals)
        res = []
        n = len(intervals)
        i,j=0,0
        min_start , max_end = intervals[0]
        '''
        idea here is to cover up all the intervals in the window i - j 
        which are overlapping. 
        How to check if they overlap ? 
        if the previous intervals end is greater than or equal to 
        the next one's start, that means that they overlap
        ''' 
        while j < n:
            if  j != (n-1) and (max_end >= intervals[j+1][0]):
                j+=1
                min_start = min(min_start,intervals[j][0])
                max_end = max(max_end,intervals[j][1])
            else:
                res.append([min_start,max_end])
                j += 1
                i = j
                if j < n:
                    min_start,max_end = intervals[j]
                
        return res
        
        
        
        
        
        