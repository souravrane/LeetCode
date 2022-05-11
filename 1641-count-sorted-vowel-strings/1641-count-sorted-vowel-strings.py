class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1: return 5
        
        arr = [1,1,1,1,1]
        for i in range(1,n):
            for j in range(3,-1,-1):
                arr[j] += arr[j+1]
        
        return sum(arr)