class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        res = []
        for k in range(n-2):
            if k == 0 or nums[k] != nums[k-1]:
                a = nums[k]
                i,j = k+1,n-1
                
                while i < j:
                    b = nums[i]
                    c = nums[j]

                    if a + b + c > 0:
                        j -= 1
                    elif a + b + c < 0:
                        i += 1
                    else:
                        res.append([a,b,c])
                        j -= 1
                        while i < j and nums[j] == c: j -= 1
        return res
        