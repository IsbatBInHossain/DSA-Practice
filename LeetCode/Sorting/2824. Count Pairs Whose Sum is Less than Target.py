from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        pairs = 0
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                d = nums[j] + nums[i]
                if d < target:
                    pairs+=1
       
        return pairs