class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            inv = intervals[i]
            prev_inv = result[-1]
            if prev_inv[1] >= inv[0]:
                prev_inv[0] = min(prev_inv[0], inv[0])
                prev_inv[1] = max(prev_inv[1], inv[1])
            else:
                result.append(inv)
        return result