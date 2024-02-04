class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        maxDepth = 0
        for c in s:
            if c == "(":
                count += 1
                maxDepth = max(maxDepth, count)
            elif c == ")":
                count -= 1
        return maxDepth
        