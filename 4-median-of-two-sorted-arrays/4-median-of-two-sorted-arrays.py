class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(B) < len(A):
            A,B = B,A
        
        total = len(A) + len(B)
        half = total // 2
        
        left = 0
        right = len(A)-1
        
        while True:
            midA = left + (right - left) // 2  
            midB = half - (midA + 1) - 1 
            
            # left partition
            Aleft = A[midA] if midA >= 0 else float('-inf')
            Bleft = B[midB] if midB >= 0 else float('-inf')
            
            # right partition
            Aright = A[midA + 1] if (midA + 1) < len(A) else float('inf')
            Bright = B[midB + 1] if (midB + 1) < len(B) else float('inf')
            
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 0:
                    return (max(Bleft, Aleft) + min(Bright, Aright)) / 2
                else:
                    return min(Bright, Aright)
                
            
            if Aleft > Bright:
                right = midA - 1
            else:
                left = midA + 1
        
            
            