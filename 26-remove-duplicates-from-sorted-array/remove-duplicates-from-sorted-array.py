class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        store = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[store-1]:
                nums[store] = nums[i]
                store += 1
        return store
        