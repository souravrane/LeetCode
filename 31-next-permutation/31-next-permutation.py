class Solution:
    def reverse(self,arr,s,e):
        while s < e:
            arr[s],arr[e] = arr[e],arr[s]
            s += 1
            e -= 1
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        leftIndex = -1
        rightIndex = n
        
        for i in range(n-1):
            if nums[i] < nums[i+1]:
                leftIndex = i

        
        if leftIndex == -1:
            self.reverse(nums,0,n-1)
            return
        
        for j in range(n-1,0,-1):
            if nums[j] > nums[leftIndex]:
                rightIndex = j
                break
        
        
        nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
        
        self.reverse(nums,leftIndex + 1,n-1)