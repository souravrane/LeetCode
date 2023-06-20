class Solution {
    public int removeDuplicates(int[] nums) {
        int left = 0, right = 0;
        while(right < nums.length) {
            // count the occurances of the num
            int count = 1;
            while(right + 1 < nums.length && nums[right] == nums[right + 1]) {
                right++;
                count++;
            }

            // replace all the left pointer values with the num
            int frequency = Math.min(count, 2);
            while(frequency > 0) {
                nums[left] = nums[right];
                left++;
                frequency--;
            }

            right++;
        }
        return left;
    }
}