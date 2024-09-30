class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        curr=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=curr: 
                curr=nums[i]
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j+=1
                
        return j
        