class Solution:
    def compress(self, chars: List[str]) -> int:
        start, end = 0, 0
        while end < len(chars):
            c = chars[end]
            count = 0
            while end < len(chars) and c == chars[end]:
                count += 1
                end += 1
            
            chars[start] = c
            start += 1
            if count > 1:
                for num in str(count): 
                    chars[start] = num
                    start += 1
        
        return start
            