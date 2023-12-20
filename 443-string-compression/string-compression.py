class Solution:
    def compress(self, chars: List[str]) -> int:
        newS = list()
        start = 0
        while start < len(chars):
            c = chars[start]
            counter = 0
            while start < len(chars) and c == chars[start]:
                counter += 1
                start += 1

            newS.append(c)
            if counter > 1: newS.extend(list(str(counter)))
        
        while chars: chars.pop()
        chars.extend(newS)
        return len(chars)


        