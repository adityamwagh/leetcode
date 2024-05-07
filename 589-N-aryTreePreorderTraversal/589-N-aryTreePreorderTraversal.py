# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        order = []
        if not root:
            return []
        
        order += [root.val]
        for child in root.children:
            if child:
                order += self.preorder(child)
        return order
[
