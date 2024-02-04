from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map = {num: i for i, num in enumerate(nums2)}
        stack = []
        result = [-1] * len(nums2)

        for i in range(len(nums2)-1, -1, -1):
            while stack and nums2[i] >= nums2[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = nums2[stack[-1]]

            stack.append(i)

        return [result[num_map[num]] for num in nums1]
