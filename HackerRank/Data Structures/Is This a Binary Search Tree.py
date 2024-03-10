""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    bst_array = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        bst_array.append(node.data)
        inorder(node.right)
    inorder(root)
    for i in range(1,len(bst_array)):
        if bst_array[i] <= bst_array[i-1]:
            return False
    return True
    