from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = []
        n = len(grid)
        for i in range(n):
            curr = []
            for j in range(n):
                curr.append(grid[j][i])
            columns.append(curr)
        
        pairCount = 0
        for row in grid:
            for column in columns:
                if row == column:
                    pairCount += 1
        return pairCount