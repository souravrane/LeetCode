class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ps, pe = 0, len(nums) - 1
        while ps < pe:
            s = nums[ps] + nums[pe]
            if s == target: return [ps + 1, pe + 1]
            if s > target: pe -= 1
            else: ps += 1
        return [ps + 1, pe + 1]
        