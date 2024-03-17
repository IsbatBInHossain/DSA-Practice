
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children


class Solution:
  def maxDepth(self, node: 'Node') -> int:
    if node is None:
      return 0
    if node.children is None:
      return 1

    max_depth = 0  # Initialize variable to store maximum depth

    for child in node.children:
      child_depth = self.maxDepth(child)  # Get child's depth
      max_depth = max(max_depth, child_depth)  # Update max_depth if needed

    return max_depth + 1  # Return overall max depth (including current node)
