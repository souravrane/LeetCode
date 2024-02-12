class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for l,r in intervals:
            if result[-1][1] < l: result.append([l,r])
            else:
                result[-1][1] = max(result[-1][1], r)
        return result 
        