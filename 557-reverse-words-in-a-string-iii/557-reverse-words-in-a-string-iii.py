class Solution:
    def reverseWord(self, sentence, s, e):
        while s < e:
            sentence[s], sentence[e] = sentence[e], sentence[s]
            s += 1
            e -= 1
        
    def reverseWords(self, s: str) -> str:
        arr = list(s)
        start = 0
        for end in range(len(arr)):
            if arr[end] == " ":
                self.reverseWord(arr,start,end-1)
                start = end
                while arr[start] == " ": start += 1
        self.reverseWord(arr, start, len(s)-1)
        
        return ''.join(arr)