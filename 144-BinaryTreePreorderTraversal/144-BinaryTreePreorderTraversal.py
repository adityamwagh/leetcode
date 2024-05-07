# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if not root:
            return []


        
        if root.right:
            vals += self.preorderTraversal(root.right)
        vals += [root.val]
        if root.left:
            vals += self.preorderTraversal(root.left)
        return vals
[
