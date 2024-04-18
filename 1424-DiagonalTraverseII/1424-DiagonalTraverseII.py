class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        q = deque([(0, 0)])  # (row, column)
        result = []
        
        while q:
            for _ in range(size):
                # handle the current element
                r, c = q.popleft()
                result.append(nums[r][c])
                
                # insert the next row
                if r + 1 < len(nums) and c == 0:
                    q.append((r + 1, 0))
                
                # insert the next column in the same row
                if c + 1 < len(nums[r]):
                    q.append((r, c + 1))
        
        return result
            size = len(q)

[
