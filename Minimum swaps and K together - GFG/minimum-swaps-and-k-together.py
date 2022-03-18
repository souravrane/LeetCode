#User function Template for python3

def minSwap (arr, n, k) : 
    #Complete the function
    windowSize = 0
    for num in arr:
        if num <= k: windowSize += 1
    
    currCount = 0
    for i in range(windowSize):
        if arr[i] <= k: currCount += 1
    
    maxCount = currCount
    
    for i in range(1,n-windowSize + 1):
        if arr[i-1] <= k:
            currCount -= 1
        
        if arr[i+windowSize-1] <= k:
            currCount += 1
            
        maxCount = max(maxCount,currCount)
    
    return windowSize - maxCount
        
    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    k = int(input())
    ans = minSwap(arr, n, k)
    print(ans)
    





# } Driver Code Ends