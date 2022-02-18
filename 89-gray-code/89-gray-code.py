'''
How to generate gray codes ?
N = 0  [0]
N = 1 => (2^0) = (01) now add 01 to all the elements in reverse order and append those values to the list : [00,01]
       
N = 2 => (2^1) = (10) repeat sanme as above : [00,01, 11, 10]

N = 3 => (2^2) = (100) : [00, 01, 11, 10, 110, 111, 101, 100]

and so on...

'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
        
        res = self.grayCode(n-1)
        
        x = 1 << (n-1)
        temp = []
        for num in res[::-1]:
            temp.append(num+x)
        
        return res + temp
        