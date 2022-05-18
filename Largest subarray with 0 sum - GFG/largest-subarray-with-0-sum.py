from collections import defaultdict
#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        hashMap = defaultdict(int)
        hashMap[0] = -1
        maxDist = 0
        curSum = 0
        for i in range(n):
            curSum += arr[i]
            if curSum in hashMap:
                maxDist = max(maxDist, i-hashMap[curSum])
            else:
                hashMap[curSum] = i
        
        return maxDist
            
        
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t= int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxLen(n ,arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends