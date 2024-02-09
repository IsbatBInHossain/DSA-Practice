from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        while nums:
            curr = []
            for i in nums[:]:
                if i not in curr:
                    curr.append(i)
                    nums.remove(i)
            res.append(curr)
        return res
            

