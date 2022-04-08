class Solution:
    def allPermutations(self, arr, permutation, res):
        if len(arr) == 0:
            res.append(permutation)
            return
        
        for i in range(len(arr)):
            num = arr[i]
            newPermutation = permutation + [num]
            newArr = []
            for j in range(len(arr)): 
                if i != j: newArr.append(arr[j])
            
            self.allPermutations(newArr, newPermutation, res)
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.allPermutations(nums, [], res)
        return res
        