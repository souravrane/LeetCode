class Solution {
    public int getNosOfDigit(int num) {
        int digit = 0;
        while(num > 0) {
            num = num / 10;
            digit++;
        }
        return digit;
    }
    
    public int findNumbers(int[] nums) {
        int result = 0;
        for(int num: nums) {
            int digits = getNosOfDigit(num);
            if(digits % 2 == 0) {
                result++;
            }
        }
        return result;
    }
}