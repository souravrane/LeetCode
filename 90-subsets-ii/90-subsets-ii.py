from collections import defaultdict

class Solution:
    def helper(self, arr, subset, index, N):
        if index == N:
            currentSub = []
            for i in range(N):
                currentSub += [arr[i][0]]*subset[i]
            self.ans.append(currentSub)
            return 
        
        freq = arr[index][1]
        for i in range(freq+1):
            newSubset = subset + [i]
            self.helper(arr, newSubset, index + 1, N)
    
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        h = defaultdict(int)
        for num in nums: h[num] += 1
        arr = []
        for k in h: arr.append((k,h[k]))
        N = len(arr)
        
        self.helper(arr, [], 0, N)
        return self.ans
        