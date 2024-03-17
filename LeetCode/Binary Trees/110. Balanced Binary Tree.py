from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def get_tree_height(self, node: Optional[TreeNode]) -> int:
        """
        This function calculates the height of a binary tree recursively.

        Args:
            node: The root node of the subtree for which height is to be determined.

        Returns:
            The height of the subtree rooted at the given node.
            -1 is returned if the subtree is not height-balanced.
        """

        if node is None:
            return 0

        left_height = self.get_tree_height(node.left)
        right_height = self.get_tree_height(node.right)

        # Check if either subtree is unbalanced (height == -1)
        if left_height == -1 or right_height == -1:
            return -1

        # Check for height difference exceeding 1 (imbalance)
        if abs(left_height - right_height) > 1:
            return -1

        # Return the maximum height of the left or right subtree + 1 (for current node)
        return max(left_height, right_height) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height = self.get_tree_height(root)
        if height == -1:
            return False
        return True
        