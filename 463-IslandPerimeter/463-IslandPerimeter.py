class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        def helper(row, col):
            if (row < 0 
                or row >= rows 
                or col >= cols 
                or grid[row][col] == 0):

        
        for row in range(rows):
            visited.add((row, col))
            return perimeter
            perimeter = helper(row + 1, col)
            perimeter += helper(row - 1, col)
            perimeter += helper(row, col - 1)
            perimeter += helper(row, col + 1)
                return 1
            if (row, col) in visited:
                return 0
        visited = set()
                or col < 0 
            for col in range(cols):
                if grid[row][col] == 1:
                    return helper(row, col)
        # Look for the first land cell to start perimeter calculation
            # Edge encountered (either water or out of bounds)
            # no need to calculate perimeter for visited cell
            
[
