
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1 = 0
        p2 = 0
        combined_nums = []
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                combined_nums.append(nums1[p1])
                p1+=1
            else:
                combined_nums.append(nums2[p2])
                p2+=1
        while p1 < len(nums1):
            combined_nums.append(nums1[p1])
            p1+=1
        while p2 < len(nums2):
            combined_nums.append(nums2[p2])
            p2+=1
        n = len(combined_nums)
        if n % 2 != 0:
            return combined_nums[(n//2)]
        else:
            return (combined_nums[n//2] + combined_nums[(n//2) -1])/2
        