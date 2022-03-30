class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        for k in range(n-2):
            if k == 0 or nums[k] != nums[k-1]:
                a = nums[k]
                target = -a
                i,j = k+1,n-1
                while i < j:
                    b = nums[i]
                    c = nums[j]

                    if b + c == target:
                        res.append([a,b,c])

                    if b + c >= target:
                        while i < j and nums[j] == c: j-=1
                    else:
                        while i < j and nums[i] == b: i+=1
        return res
        