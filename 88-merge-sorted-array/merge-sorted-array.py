class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2, mp = m-1, n-1, len(nums1) - 1
        while (p1 >= 0 and p2 >= 0):
            if(nums1[p1] > nums2[p2]):
                nums1[mp] = nums1[p1]
                p1 -= 1
            else:
                nums1[mp] = nums2[p2]
                p2 -= 1
            mp -= 1

        while p2 >= 0:
            nums1[mp] = nums2[p2]
            p2 -= 1
            mp -= 1
        

