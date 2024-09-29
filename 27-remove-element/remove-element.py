class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size, store = 0, 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[store] = nums[i]
                store += 1
                size += 1
        return size
        