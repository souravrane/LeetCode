class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = list()
        n = len(intervals)
        i = 0

        # no overlap before the merge
        while i < n and intervals[i][1] <  newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        # overlap and merge
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        result.append(newInterval)

        # no overlap, after merge
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
        