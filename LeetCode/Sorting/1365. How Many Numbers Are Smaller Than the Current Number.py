from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        idx_nums = sorted(range(len(nums)), key=lambda k: nums[k])
        ans = [0] * len(nums)

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                ans[idx_nums[i]] = ans[idx_nums[i - 1]]
            else:
                ans[idx_nums[i]] = i

        return ans