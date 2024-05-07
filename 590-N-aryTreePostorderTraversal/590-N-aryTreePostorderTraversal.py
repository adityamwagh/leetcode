"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        order = []
        if not root:
            return []
        for child in root.children:
            if child:
                order += self.postorder(child)
        order += [root.val]
        return order
[
