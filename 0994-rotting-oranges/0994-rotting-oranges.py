class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # when to stop? when all oranges are rotten
        # time elapsed untill all are rotten is the answer
        fresh = 0
        queue = deque()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0)) # collect rotten oranges
                elif grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while queue:

            r, c, step = queue.popleft()
            minutes = step

            # visit neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1):
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, step + 1))
        
        print(fresh, minutes)
        return minutes if fresh == 0 else -1

