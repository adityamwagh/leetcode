# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        leftSum = 0
        
            return 0
        if root.left:
        
        
            if not root.left.left and not root.left.right:
                leftSum += root.left.val
            else:
                leftSum += self.sumOfLeftLeaves(root.left)
        leftSum += self.sumOfLeftLeaves(root.right)

        if root is None:
        return leftSum
[
