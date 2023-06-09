class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0, countOnes = 0;
        for(int i=0; i<nums.length; i++) {
            int num = nums[i];
            if(num == 1) {
                countOnes++;
                result = Math.max(result, countOnes);
            } else {
                countOnes = 0;
            }
        }
        return result;
    }
}