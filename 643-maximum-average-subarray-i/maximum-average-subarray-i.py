class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        Ksum = sum(nums[:k])
        maxAvg = Ksum / k
        for i in range(k, len(nums)):
            Ksum += nums[i] - nums[i-k]
            maxAvg = max(maxAvg, Ksum / k)
        return maxAvg
        