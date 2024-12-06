class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = list()
        points.sort()
        result.append(points[0])
        for i in range(1, len(points)):
            xs, xe = points[i]
            cs, ce = result[-1]
            if ce >= xs: # update the last interval with the difference
                result[-1] = [max(xs, cs), min(xe, ce)]
            else:
                result.append(points[i])
        return len(result)