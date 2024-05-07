# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        if not root:
            return []
        return vals

# Definition for a binary tree node.
        if root.left:
            vals += self.postorderTraversal(root.left)
        vals += [root.val]
        if root.right:
            vals += self.postorderTraversal(root.right)
        
[
