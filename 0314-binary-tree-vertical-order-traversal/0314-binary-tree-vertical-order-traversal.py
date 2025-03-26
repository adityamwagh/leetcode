from collections import deque, defaultdict
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Handle empty tree case
        if not root:
            return []
        
        # Use a queue to do level-order traversal
        # Each element in queue is (node, column)
        queue = deque([(root, 0)])
        
        # Use an ordered dictionary to store nodes by column
        order = defaultdict(list)
        
        # Track min and max columns to order the final result
        min_col, max_col = 0, 0
        
        while queue:
            # Process current level
            level_size = len(queue)
            for _ in range(level_size):
                node, col = queue.popleft()
                
                # Add node's value to its column
                order[col].append(node.val)
                
                # Update column range
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                
                # Add left and right children to queue
                if node.left:
                    queue.append((node.left, col - 1))
                if node.right:
                    queue.append((node.right, col + 1))
        
        # Return columns from min to max
        return [order[col] for col in range(min_col, max_col + 1)]