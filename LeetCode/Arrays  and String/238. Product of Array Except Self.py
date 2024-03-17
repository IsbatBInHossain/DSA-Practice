from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProducts = [1]
        rightProducts = [1]

        current = 1
        for i in range(1, n):
            current = current * nums[i-1]
            leftProducts.append(current)
        
        current = 1
        for j in range(n-2, -1, -1):
            current = current * nums[j+1]
            rightProducts.append(current)

        return [leftProducts[i] * rightProducts[n-i-1] for i in range(n)]
        