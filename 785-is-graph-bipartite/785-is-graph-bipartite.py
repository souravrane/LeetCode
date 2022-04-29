class Solution:
     def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n, colored = len(graph), {}
        def dfs_color(color, idx, graph, colored):
            if idx in colored:
                return color == colored[idx]
            colored[idx] = color                            
            return all(dfs_color(-color, nb, graph, colored) for nb in graph[idx])
    
        return all(i in colored or dfs_color(1, i, graph, colored) for i in range(n)) 	