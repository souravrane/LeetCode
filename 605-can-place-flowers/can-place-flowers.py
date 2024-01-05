class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start = -1
        count = 0
        result = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0: count += 1
            else:
                if start == -1:
                    result += floor(count / 2)
                else:
                    result += floor((count - 1) / 2)
                    
                start = i
                print(flowerbed[start:i+1], count)
                count = 0
        
        if start > -1 and count != 0: result += floor(count / 2)
        else: result += ceil(count / 2)
        return result >= n
    '''
    1 - 0
    2 - 0
    3 - 1
    4 - 1
    5 - 2
    6 - 2

    '''