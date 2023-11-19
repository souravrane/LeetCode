class Solution:
    def rev(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        self.rev(nums, 0, len(nums) - 1)
        self.rev(nums, 0, k-1)
        self.rev(nums, k, len(nums) - 1)

        
        