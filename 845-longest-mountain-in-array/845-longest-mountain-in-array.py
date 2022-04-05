class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3: return 0
        
        longestMountain = 0
        
        '''
        We look for a peak by checking its prev and next element
        If its a peak, then move left and right and count how many
        elements are part of the decreasing sequence.
        
        update the longest Mountain.
        
        '''
        for i in range(1,n-1):
            
            # Its a peak !
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                
                leftRange = 0
                for k in range(i-1,-1,-1):
                    if arr[k] < arr[k+1]:
                        leftRange += 1
                    else:
                        break
                
                rightRange = 0
                for k in range(i+1,n):
                    if arr[k-1] > arr[k]:
                        rightRange += 1
                    else:
                        break
                
                currMountain = leftRange + rightRange + 1
                longestMountain = max(longestMountain, currMountain)
        
        
        return longestMountain
        