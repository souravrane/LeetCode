class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattanDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                dist = manhattanDist(points[i], points[j])
                graph[i].append([j, dist])
                graph[j].append([i, dist])

        def prime(src):
            seen = set()
            minHeap = [[0, src]]  # pair of (dist, vertex)
            totalDist = 0
            while len(seen) < n:
                dist, u = heapq.heappop(minHeap)
                if u in seen: continue
                seen.add(u)
                totalDist += dist
                for v, d in graph[u]:
                    if v not in seen:
                        heapq.heappush(minHeap, [d, v])
            return totalDist
        
        return prime(0)