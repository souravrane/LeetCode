class Solution {
    public int removeDuplicates(int[] nums) {
        LinkedHashSet<Integer> set = new LinkedHashSet<Integer>();
        for(int x : nums) set.add(x);
        int i = 0;
        for(int ele : set) {
            nums[i]  = ele;
            i++;
        }
        return set.size();
    }
}