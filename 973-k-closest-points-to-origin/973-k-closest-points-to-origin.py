import heapq

def euclideanDist(x,y):
    return x*x + y*y

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        
        for x,y in points:
            distance = -euclideanDist(x,y)
            if k == 0:
                heapq.heappushpop(res, (distance, x, y))
            else:
                heapq.heappush(res, (distance, x, y))
                k -= 1
        
        return [[x,y] for d,x,y in res]
        