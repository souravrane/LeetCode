class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 2: return size

        store = 2
        for i in range(2, size):
            if nums[i] != nums[store - 1] or (nums[i] != nums[store-2]):
                nums[store] = nums[i]
                store += 1
        return store
        