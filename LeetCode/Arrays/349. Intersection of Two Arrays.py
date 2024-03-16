from typing import List


class Solution:
    def list_to_map(self,array):
        hashMap = {}
        for item in array:
            hashMap[item] = True
        return hashMap

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        nums1_map = self.list_to_map(nums1)
        nums2_set = set(nums2)
        for i in nums2_set:
            if i in nums1_map:
                arr.append(i)
        return arr