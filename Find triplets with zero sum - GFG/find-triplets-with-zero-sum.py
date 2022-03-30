#User function Template for python3

class Solution:
    def twoSum(self, nums, target):
        s = set()
        n = len(nums)
        for i in range(n):
            if target-nums[i] in s:
                return 1
            s.add(nums[i])
        return 0
        
    #Function to find triplets with zero sum.    
    def findTriplets(self, nums, n):
        #code here
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            x = self.twoSum(nums[i+1:],target)
            if x == 1:
                return 1
        
        return 0
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        a=list(map(int,input().strip().split()))
        if(Solution().findTriplets(a,n)):
            print(1)
        else:
            print(0)
# } Driver Code Ends