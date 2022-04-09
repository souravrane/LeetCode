from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Bucket sort trick
        
        we basically want to sort the array w.r.t count, without really sorting it
        So create another array of size N.
        Now let the index values in this array represent your count.
        
        All we have to do is count the number of each distinct element in the original array
        and store it in the new array where index == count(element)
        
        Once we are done with that , we can traverse from the end in the sorted fashion
        and pick out top k elements
        
        '''
        n = len(nums)
        h = defaultdict(int)
        
        for num in nums: h[num] += 1
        
        countArray = [[] for i in range(n+1)]
        
        for key,val in h.items():
            index = val
            countArray[index].append(key)
        
        res = []
        for i in range(n,-1,-1):
            arr = countArray[i]
            
            res = res + arr
            k -= len(arr)

            if k == 0: break
        
        return res