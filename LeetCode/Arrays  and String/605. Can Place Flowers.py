from typing import List


class Solution:
    def isPlantable(self, flowerbed: List[int], index: int) -> bool:
        n = len(flowerbed)
        
        if flowerbed[index] == 1:
            return False
        if n == 1:
            return True
        if index == 0:
            return flowerbed[index + 1] == 0  
        if index == n - 1:
            return flowerbed[index - 1] == 0 

        return flowerbed[index - 1] == 0 and flowerbed[index + 1] == 0


    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while n and i < len(flowerbed):
            if self.isPlantable(flowerbed, i):
                n -= 1
                flowerbed[i] = 1
            i += 1
        return n == 0