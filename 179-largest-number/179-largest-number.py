from functools import cmp_to_key

def compare(a,b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    if int(ab) > int(ba):
        return -1
    return 1

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = sorted(nums, key=cmp_to_key(compare))
        res = ''
        for i in nums:
            res += str(i)
        if res.count('0') == len(res) : return '0'
        return res