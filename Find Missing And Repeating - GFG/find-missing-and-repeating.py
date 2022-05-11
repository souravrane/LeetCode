#User function Template for python3

class Solution:
    def findTwoElement( self, arr, n): 
        # 1 3 3 
        # code here
        xor = 0
        for num in arr:
            xor ^= num 
        
        for num in range(1,n+1):
            xor ^= num
            
        
        # divide numbers into 2 groups based on the last set bit
        mask = xor & ~(xor-1)
        
        group1 = 0
        group2 = 0
        
        for num in range(1,n+1):
            if mask & num != 0:
                group1 ^= num
            else:
                group2 ^= num
        
        for num in arr:
            if mask & num != 0:
                group1 ^= num
            else:
                group2 ^= num
        
        if group1 in arr:
            return [group1, group2]
        
        return [group2, group1]
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends