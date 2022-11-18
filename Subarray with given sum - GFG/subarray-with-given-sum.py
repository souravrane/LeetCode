#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self, arr, size, target):
        if size < 2: return [-1]
            
        i = -1
        curSum = 0
        for j in range(size):
            curSum += arr[j]
            
            while curSum > target:
                i += 1
                curSum -= arr[i]

            if curSum == target:
                if target == 0:
                    if sum(arr[i+2:j+1]) != 0: continue
                else:
                    return [i + 2, j + 1] 
                
        return [-1]
       


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends