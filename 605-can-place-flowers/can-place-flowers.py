class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        start, count = -1, 0
        result = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0: count += 1
            else:
                result += floor((count - 1) / 2) if start > -1 else floor(count / 2)
                count = 0
                start = i
        result += floor(count / 2) if start != -1 and count != 0 else ceil(count / 2)
        return result >= n

                
