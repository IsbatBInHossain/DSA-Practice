from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_array = [0]
        right_array = [0]
        n = len(nums)
        [left_array.append(nums[i] + left_array[-1]) for i in range(n - 1)]
        [right_array.append(nums[i] + right_array[-1]) for i in range(n - 1, 0, -1)]
        right_array.reverse()

        for i in range(n):
            if left_array[i] == right_array[i]:
                return i
        return -1
        