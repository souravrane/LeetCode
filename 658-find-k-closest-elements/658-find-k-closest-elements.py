class Solution:
    def binarySearch(self, arr, target):
        left = 0
        right = len(arr) - 1
        ans = 0
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
            if abs(arr[mid] - target) < abs(arr[ans]- target):
                    ans = mid
        return ans
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        position = self.binarySearch(arr,x)
        i,j = position,position
        
        while k > 1:
            left = arr[i-1] if i > 0 else float('-inf')
            right = arr[j + 1] if j < len(arr)-1 else float('inf')
            
            if x - left <= right - x:
                i -= 1
            else:
                j += 1
                
            k -= 1
        
        return arr[i:j+1]
            
            
            
            
            
             