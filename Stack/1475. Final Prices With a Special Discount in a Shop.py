from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = [None]*len(prices)
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    result[i] = prices[i] - prices[j]
                    break
            if result[i] == None:
                result[i] = prices[i]
        return result