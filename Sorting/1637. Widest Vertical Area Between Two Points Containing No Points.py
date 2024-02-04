from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_coords = []
        for point in points:
            x_coords.append(point[0])
        x_coords.sort()
        max_diff = 0
        for i in range(1,len(x_coords)):
            d = x_coords[i] - x_coords[i-1]
            max_diff = max(max_diff, d)
        return max_diff