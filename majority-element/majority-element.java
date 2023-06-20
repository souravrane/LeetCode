class Solution {
    public int majorityElement(int[] nums) {
        int majority = nums[0];
        int count = 1;

        for(int i = 1; i < nums.length; i++) {
            int curNum = nums[i];
            
            if(count == 0) {
                majority = curNum;
                count = 1;
                continue;
            }

            if(majority == curNum) count++;
            else count--;
        }

        return majority;
    }
}