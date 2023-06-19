class Solution {
    public int removeDuplicates(int[] nums) {
        int lastUnique = 0;
        for(int i = 1; i < nums.length; i++) {
            if(nums[i-1] != nums[i]) {
                lastUnique++;
                nums[lastUnique] = nums[i];
            }
        }
        return lastUnique + 1;
    }
}