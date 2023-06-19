class Solution {
    public int removeDuplicates(int[] nums) {
        if(nums.length == 0) return 0;

        HashSet<Integer> numsVisited = new HashSet<Integer>();
        numsVisited.add(nums[0]);

        int lastNonDup = 1, k = 1;
        for(int i = 1; i < nums.length; i++) {
            int num = nums[i];
            if(numsVisited.contains(num)) continue;

            nums[lastNonDup] = num;
            numsVisited.add(num);
            lastNonDup++;
        }

        return numsVisited.size();
    }
}