class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters)-1
        
        if letters[-1] <= target: return letters[0]
        
        ans = 0
        
        while left <= right:
            
            mid = left + (right - left) // 2
                
            if letters[mid] <= target:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
                
        
        return letters[ans]