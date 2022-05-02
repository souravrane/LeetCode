class Solution:
    def findMedian(self, nums1, nums2, half):
        def check(mid):
            count1,count2 = 0,0
            for i in nums1:
                if i <= mid: count1 += 1
            for i in nums2:
                if i <= mid: count2 += 1

            return count1 + count2 >= half
        if nums1 and nums2:
            left = min(nums1[0], nums2[0])
            right = max(nums1[-1], nums2[-1])
        elif nums1:
            left = nums1[0]
            right = nums1[-1]
        elif nums2:
            left = nums2[0]
            right = nums2[-1]
        else:
            left = right = 0
            
        ans = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return ans
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        
        if total % 2 == 0:
            median1 = self.findMedian(nums1, nums2, total // 2 ) 
            median2 = self.findMedian(nums1, nums2, (total // 2) + 1 )
            return (median1 + median2) / 2
        else:
            return self.findMedian(nums1, nums2, total // 2 + 1)
            
        