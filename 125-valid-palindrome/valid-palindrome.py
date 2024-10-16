class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = list()
        for char in s:
            if char.isalnum(): result.append(char.lower())
        s,e = 0, len(result)-1
        while s < e:
            if result[s] != result[e]: return False
            s += 1
            e -= 1
        return True