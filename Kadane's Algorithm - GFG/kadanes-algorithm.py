#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        maxSum = float('-inf')
        curSum = 0
        
        for i in range(len(arr)):
            curSum += arr[i]
            
            if curSum < arr[i]:
                curSum = arr[i]
            
            maxSum = max(maxSum, curSum)
        
        return maxSum
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends