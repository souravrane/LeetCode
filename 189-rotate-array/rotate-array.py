class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k:
            self.reverse(nums, 0, len(nums)-1)
            self.reverse(nums, 0, k-1)
            self.reverse(nums, k, len(nums)-1)