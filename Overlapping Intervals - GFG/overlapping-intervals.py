from functools import cmp_to_key

class Solution:
    def compare(self, a, b):
        if a[0] > b[0]: return 1
        return -1
        
	def overlappedInterval(self, Intervals):
	    Intervals = sorted(Intervals, key = cmp_to_key(self.compare))
	    res = [Intervals[0]]
	    
	    for i in range(1,len(Intervals)):
	        interval = Intervals[i]
	        
	        if interval[0] <= res[-1][1]:
	            res[-1][0] = min(interval[0], res[-1][0])
	            res[-1][1] = max(interval[1], res[-1][1])
	        else:
	            res.append(interval)
	   
	    return res
 
#{ 
#  Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends