#User function Template for python3
class Solution:
    def gcd(self, a, b):
        if a == 0: return b
        return self.gcd(b%a, a)
    
    def rooms(self, N, M):
        # code here
        ans = self.gcd(N,M)
        return (N + M) // ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, M = [int(x) for x in input().split()]
        
        ob = Solution()
        print(ob.rooms(N, M))
# } Driver Code Ends