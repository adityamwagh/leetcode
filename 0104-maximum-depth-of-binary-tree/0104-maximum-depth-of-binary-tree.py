# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
            
        stack = []
        max_depth = 0
        stack.append((root, 1))

        while stack:

            curr, curr_depth = stack.pop()
            max_depth = max(max_depth, curr_depth)

            if curr.left:
                stack.append((curr.left, curr_depth + 1))
            if curr.right:
                stack.append((curr.right, curr_depth + 1))
        
        return max_depth
            
