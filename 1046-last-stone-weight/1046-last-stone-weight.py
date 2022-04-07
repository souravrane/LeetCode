class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones.sort()
        
        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
            res = abs(first-second)
            stones.append(res)
            stones.sort()
        
        return stones[-1]
            
        