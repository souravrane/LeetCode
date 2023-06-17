class Solution {
    public int removeElement(int[] nums, int val) {
        int start = 0, end = nums.length - 1, k = 0;
        while(start < end) {
            if(nums[start] == val) {
                while(end > start && nums[end] == val) end--;
                if(end > start) {
                    int temp = nums[start];
                    nums[start] = nums[end];
                    nums[end] = temp;
                    end--;
                }
            }

            start++;
        }
        
        for(int x: nums) if(x != val) k++;
        return k;
    }
}