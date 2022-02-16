class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse_arr(A,s,e):
            if s>=e: return
            A[s],A[e] = A[e],A[s]
            reverse_arr(A,s+1,e-1)
        
        n = len(s)-1
        reverse_arr(s,0,n)
        
        
        