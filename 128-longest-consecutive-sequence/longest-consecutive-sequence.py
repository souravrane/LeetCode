class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visited = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in visited: continue
            count, temp = 0, num
            while temp in visited:
                count += 1
                temp += 1
            longest = max(longest, count)
        return longest