class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points = sorted(points, key = lambda x:x[1])
        end = list()
        for i in range(len(points)):
            xs, xe = points[i]
            if end: cs, ce = end
            if end and ce >= xs: # update the last interval with the difference
                end = [max(xs, cs), min(xe, ce)]
            else:
                count += 1
                end = points[i]
        return count