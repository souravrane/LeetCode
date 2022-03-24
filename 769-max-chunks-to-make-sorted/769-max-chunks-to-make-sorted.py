class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        Chaining technique
        '''
        n = len(arr)
        maxSoFar = 0
        count = 0
        
        for i in range(n):
            maxSoFar = max(maxSoFar, arr[i])
            if i == maxSoFar :
                count += 1
        
        
        return count
        