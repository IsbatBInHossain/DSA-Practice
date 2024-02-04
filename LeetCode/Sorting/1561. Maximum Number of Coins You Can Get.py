from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_piles = sorted(piles, reverse=True)
        coins = 0
        n = len(piles)//3
        for i in range(1, n*2, 2):
            coins += sorted_piles[i]
        return coins