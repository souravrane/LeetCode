class Solution:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if arr[mid] == target: return True
            
            if arr[mid] < target: 
                left = mid + 1
            else:
                right = mid - 1
        
        return False
    
    
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        
        nums1.sort()
        res = []
        for i in set(nums2):
            if self.binarySearch(nums1, i):
                res.append(i)
        
        return res
        