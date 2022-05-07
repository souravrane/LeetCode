class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False

        min_nums = [nums[0]]
        for i in range(1, len(nums)):
            min_nums.append(min(nums[i], min_nums[-1]))
            
        stack = []  
        i = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            # 4
            if( nums[i] > min_nums[i] ):
                # 5
                while( stack and stack[-1] <= min_nums[i] ):
                    stack.pop()
                # 6
                if(stack and min_nums[i] < stack[-1] < nums[i] ):
                    return True
                # 4
                stack.append(nums[i])
        return False       