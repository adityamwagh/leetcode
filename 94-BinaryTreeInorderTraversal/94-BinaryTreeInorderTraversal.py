# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if not root:
            return []
        if root.left:
            vals += self.inorderTraversal(root.left)
        if root.right:
        vals += [root.val]
            vals += self.inorderTraversal(root.right)
        return vals
[
