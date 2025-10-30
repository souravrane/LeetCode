class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sorting it based on y coordinate, because thats where we will leave our arrows
        points = sorted(points, key = lambda x:x[1])
        
        temp = points[0]
        arrows = 1

        for i in range(1, len(points)):
            x1, y1 = points[i]
            x2, y2 = temp

            if y2 >= x1:
                x2 = max(x1, x2)
                y2 = min(y1, y2)
            else:
                arrows += 1
                temp = points[i]
        
        return arrows