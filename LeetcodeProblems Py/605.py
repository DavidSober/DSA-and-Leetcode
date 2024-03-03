class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        count = n
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            return False
        if len(flowerbed) == 2 and flowerbed == [0,0] and n == 1:
            return True
        elif len(flowerbed) == 2:
            return False
        tyype = list(set(flowerbed))
        if len(tyype) == 1 and tyype[0] == 0: # all zeros
            if len(flowerbed) % 2 == 0 and n <= (len(flowerbed) // 2): # even zeros
                return True
            elif len(flowerbed) % 2 != 0 and n <= (len(flowerbed) // 2) + 1: # odd zeros
                return True
            else:
                return False
            
        if len(flowerbed) >= 3:
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                flowerbed[0] == 1
                count -= 1
            if flowerbed[-1] == 0 and flowerbed[-2] == 0:
                flowerbed[-1] == 1
                count -= 1
        
        for i in range(1, len(flowerbed) - 2):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                count -= 1
                flowerbed[i] = 1
            if count <= 0:
                return True
        if count <= 0:
            return True
        return False