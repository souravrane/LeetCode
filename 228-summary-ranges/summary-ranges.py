class Solution:
    def formatString(self, start, end, count):
        if count == 1: return str(start)
        return str(start) + "->" + str(end)

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        ranges = list()
        start = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i]-nums[i-1] > 1:
                ranges.append(self.formatString(start, nums[i-1], count))
                start = nums[i]
                count = 0
            count += 1
        ranges.append(self.formatString(start, nums[-1], count))
        return ranges        