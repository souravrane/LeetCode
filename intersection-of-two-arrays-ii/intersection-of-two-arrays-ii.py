class Solution:
    
    def firstOccurance(self, arr, target):
        left = 0
        right = len(arr) - 1
        
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                ans = mid
                right = mid - 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
    def lastOccurance(self, arr, target):
        left = 0
        right = len(arr) - 1
        
        ans = -1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                ans = mid
                left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
    
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        
        res = []
        for i in range(len(nums1)):
            target = nums1[i]
            if i == 0 or nums1[i] != nums1[i-1]:
                n1f = self.firstOccurance(nums1, target)
                n1l = self.lastOccurance(nums1, target)
                
                n2f = self.firstOccurance(nums2, target)
                n2l = self.lastOccurance(nums2, target)
                
                if n2f != -1:
                    res += [target]*min( n1l - n1f + 1, n2l - n2f + 1)
        
        return res