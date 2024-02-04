from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        max_like = 0
        curr_like = 0

        for s in satisfaction:
            curr_like += s
            if curr_like > 0:
                max_like += curr_like
            else:
                break

        return max_like