    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def helper(root, curStr):
            if not root:
                return
            
            
            # return appropriate strings if only one child exixts
            if root.left:
            # root val is integer, where a = 0, z = 25
            # so we must get the correct ascii value and change it
            # REMEMBER TO ADD THE ROOT VALUE FIRST OR ELSE WE WILL GET THE REVERSED STRING
            curStr = chr(ord("a") + root.val) + curStr

            # return the smaller string out of both children if they exist
            if root.left and root.right:
                return min(helper(root.left, curStr), helper(root.right, curStr))
                return helper(root.left, curStr)
            if root.right:
                return helper(root.right, curStr)
            
            return curStr
        
        return helper(root, "")
class Solution:
#         self.right = right
#         self.left = left
[
