class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p_count = dict()
        s_count = dict()
        s_arr = s.split(' ')

        if len(pattern) != len(s_arr): return False

        for i in range(len(pattern)):

            left, right = pattern[i], s_arr[i]

            if left in p_count and p_count[left] != right: return False
            if right in s_count and s_count[right] != left: return False

            p_count[left] = right
            s_count[right] = left
        
        return True