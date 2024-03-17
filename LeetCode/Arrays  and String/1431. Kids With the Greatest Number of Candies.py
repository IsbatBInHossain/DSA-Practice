from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        current_max = max(candies)
        greatest_candies = [(current_candies + extraCandies) >= current_max for current_candies in candies]
        return greatest_candies
        