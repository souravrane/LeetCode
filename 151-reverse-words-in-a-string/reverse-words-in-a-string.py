class Solution:
    def reverseWords(self, s: str) -> str:
        ans = list()
        words = s.split(" ")
        words = words[::-1]
        for w in words:
            if w != "": ans.append(w)
        return " ".join(ans)        

        