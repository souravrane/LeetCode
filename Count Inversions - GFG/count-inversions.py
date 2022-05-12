class Solution:
    #User function Template for python3
    
    def mergeSort(self,arr, s, e):
        if s == e:
            return 0
        
        mid = s + (e - s) // 2
        
        li = self.mergeSort(arr, s, mid)
        ri = self.mergeSort(arr,mid+1,e)
        ci = self.merge(arr,s,mid,e)
        
        return li + ri + ci
        
    # [2, 4,] [1, 3, 5]
    def merge(self, arr,s,mid,e):
        res = []
        invCount = 0
        
        
        # merge
        i = s
        j = mid + 1
        
        
        while i <= mid and j <= e:
            if arr[i] <= arr[j]:
                res.append(arr[i])
                i +=1 
                
            else:
                invCount += (mid - i) + 1
                res.append(arr[j])
                j += 1
        
        while i <= mid:
            res.append(arr[i])
            i += 1
        
        while j <= e:
            res.append(arr[j])
            j += 1
        
        for i in range(len(res)):
            arr[s+i] = res[i]
            
        return invCount

    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        count = self.mergeSort(arr,0,n-1)
        return count
    
    
    
   
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
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends