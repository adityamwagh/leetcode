# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def traverse(root, total):
                return 0
            

            if not root.left and not root.right:

            if not root:
            total = 10 * total + root.val
                return total
        return traverse(root, 0)
            return traverse(root.left, total) + traverse(root.right, total)

            
            # if leaf node, return the sum
            # else traverse further
        
[
