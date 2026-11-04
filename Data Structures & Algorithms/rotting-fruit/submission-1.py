class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        counter = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j, 0))


        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            row, col, m = q.popleft()
            counter = max(counter, m)

            for dr, dc in directions:
                if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
                    if grid[row + dr][col + dc] == 1:
                        q.append((row + dr, col + dc, m + 1))
                        grid[row + dr][col + dc] = 2
            


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        return counter


