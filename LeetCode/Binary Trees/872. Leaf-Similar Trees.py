from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafValue(self, node: Optional[TreeNode]) -> List[int]:
        if node is None:
            return []

        if node.left is None and node.right is None:
            return [node.val]

        left_leaves = self.leafValue(node.left)
        right_leaves = self.leafValue(node.right)
        return left_leaves + right_leaves 
    

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_sequence = self.leafValue(root1) 
        root2_sequence = self.leafValue(root2)
        return root1_sequence == root2_sequence
