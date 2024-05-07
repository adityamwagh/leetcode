    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root1 and not root2:  # If both nodes are None, they are mirrors
            return True
        if not root1 or not root2:  # If only one node is None, they are not mirrors
            return False
        if root1.val != root2.val:  # If the values are different, they are not mirrors
            return False

        # Recursively check if the left subtree of root1 is a mirror of the right subtree of root2,
        # and the right subtree of root1 is a mirror of the left subtree of root2
        return self.areMirror(root1.left, root2.right) and self.areMirror(root1.right, root2.left)
        if not root or (not root.left and not root.right):
            return True
        if root.left and root.right:
            return self.areMirror(root.left, root.right)

        return False
[
