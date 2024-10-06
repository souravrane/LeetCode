class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        paperCounts = [0]*(n+1)

        for c in citations: paperCounts[min(c, n)] += 1

        h = n
        papers = paperCounts[h]
        while papers < h:
            h -= 1
            papers += paperCounts[h]
        
        return h
