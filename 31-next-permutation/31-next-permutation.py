class Solution:
    def reverseList(self,nums,i,j):
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1

        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        '''
        Element of interest :
        The element thats smaller 
        than the right most strictly decreasing section
        
        For example:
        
        6 2 1 5 4 3 0
            ^
        
        The element of interest here is 1.
        The numbers to right of 1 are in the decreasing order, that means
        we have reached the max permutation with 1 at that place.
        Now the next thing would be to replace 1 with the next number greater than 1 to its right which would be 3.
        
        6 2 3 [5 4 1 0]
        
        Now after replacement we see that the section to the right is still decreasing, which means that its again the last permutation 
        of 3 in that place. So in order to get the smallest or next permutation of the arrangement we sorted all the numbers to its right
        
        As the numbers are already placed in the decreasing order, all we need to do is reverse the right side
        
        '''

        n = len(nums)
        
        if n == 1: return
        if n == 2: 
            self.reverseList(nums,0,1)
            return
            
        indexOfInterest = -1
        
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                indexOfInterest = i
                break
           
        if indexOfInterest == -1:
            self.reverseList(nums,0,n-1)
            return        
        
        for i in range(n-1,-1,-1):
            if nums[i] > nums[indexOfInterest]:
                nums[i],nums[indexOfInterest] = nums[indexOfInterest], nums[i]
                break
        
        self.reverseList(nums, indexOfInterest+1, n-1)
        
        
        