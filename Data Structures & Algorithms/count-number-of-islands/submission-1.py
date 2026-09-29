class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def traverse(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == '0':
                return
            
            grid[i][j] = '0'

            traverse(i, j + 1)
            traverse(i, j - 1)
            traverse(i + 1, j)
            traverse(i - 1, j)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    traverse(i, j)
                
        return count
