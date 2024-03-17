from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.minDepth(node.left)
        right = self.minDepth(node.right)
        depth = 0

        if left == 0:
            depth = right
        elif right == 0:
            depth = left
        else:
            depth = min(right, left)

        return depth + 1
        