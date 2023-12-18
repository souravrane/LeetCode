class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        s = list(s)
        start, end = 0, len(s) - 1
        while (True):
            while start < end and s[start] not in vowels:
                start += 1
            
            while start < end and s[end] not in vowels:
                end -= 1
            
            if start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            else:
                break

        return ''.join(s)