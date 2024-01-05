class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start, count = -1, 0
        result = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0: count += 1
            else:
                if start > -1 :
                    result += floor((count - 1) / 2)
                else:
                    result += floor(count / 2)
                count = 0
                start = i
        if start != -1 and count != 0: result += floor(count / 2)
        else: result += ceil(count / 2)
        return result >= n

                
