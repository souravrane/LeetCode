class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        n = len(l)
        
        for i in range(n):
            left = l[i]
            right = r[i]
            arr = sorted(nums[left:right+1])
            if len(arr) <= 2: res.append(True)
            else:
                flag = 1
                cd = arr[1]-arr[0]
                for j in range(2,len(arr)):
                    if arr[j] - arr[j-1] != cd:
                        flag = 0
                        break
                if flag == 1: res.append(True)
                else: res.append(False)
        
        return res