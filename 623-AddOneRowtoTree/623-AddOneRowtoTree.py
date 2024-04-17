#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        def traverse(root, val, depth, curDepth):
            if depth == 1:
                tmp = TreeNode(val)
                tmp.left = root
                return tmp
            if not root:
                return root
            
            if curDepth == depth - 1:
                tmpL, tmpR = root.left, root.right
                root.left, root.right = TreeNode(val), TreeNode(val)
                root.left.left, root.right.right = tmpL, tmpR
                return root
            
            root.left = traverse(root.left, val, depth, curDepth + 1)
            root.right = traverse(root.right, val, depth, curDepth + 1)

            return root
        
        return traverse(root, val, depth, 1)

[
