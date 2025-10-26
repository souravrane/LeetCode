class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        for i in range(len(s)):
            left = s[i]
            right = t[i]

            if left in s_map and s_map[left] != right: return False
            if right in t_map and t_map[right] != left: return False

            s_map[left] = right
            t_map[right] = left
        
        return True



        