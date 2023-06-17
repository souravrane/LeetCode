class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int p1 = m-1, p2 = n-1, k = m + n - 1;
        while(p1 >= 0 && p2 >= 0) {
            int firstNum = nums1[p1];
            int secondNum = nums2[p2];
            if(firstNum > secondNum) {
                nums1[k] = firstNum;
                p1--;
            } else {
                nums1[k] = secondNum;
                p2--;
            }
            k--;
        }

        while(p1 >= 0) {
            int num = nums1[p1];
            nums1[k] = num;
            p1--;
            k--;
        }

        while(p2 >= 0) {
            int num = nums2[p2];
            nums1[k] = num;
            p2--;
            k--;
        }
    }
}