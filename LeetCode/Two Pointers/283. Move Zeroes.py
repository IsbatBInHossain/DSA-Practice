from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 1:
            return
        for i in range(n-1, -1, -1):
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
        