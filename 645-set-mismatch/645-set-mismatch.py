class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = set()
        repeated_num = 0
        missing_num = 0
        
        for n in nums:
            if n in s: 
                repeated_num = n
            s.add(n)
        
        print(s)
        
        for i in range(1,len(nums)+1):
            if i not in s: 
                return [repeated_num,i]
            
            
                
        