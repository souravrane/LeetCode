class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for [l,r] in intervals:
            if result[-1][1] >= l:
                result[-1] = [min(result[-1][0], l), max(result[-1][1],r)]
            else:
                result.append([l,r])
        return result