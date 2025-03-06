class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a, b = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] in seen:
                    b = grid[i][j]
                else:
                    seen.add(grid[i][j])
        
        for n in range(1, len(grid)**2 + 1):
            if n not in seen:
                a = n
        
        
        return [b, a]