class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through every tile
        # if tile==1: 
        #   travel(tile coordinate) => travel u,d,r,l and mark all 
        #   adjacent tiles as 0's
        # once that's done, numOfIslands++

        num_rows = len(grid)
        num_cols = len(grid[0])
        total_islands = 0

        def _travel_island(i, j):
            if not (i >= 0 and j >= 0 and i < num_rows and j < num_cols) or grid[i][j] == "0":
                return

            grid[i][j] = "0"
            _travel_island(i+1, j)
            _travel_island(i-1,j)
            _travel_island(i,j+1)
            _travel_island(i,j-1)
        
        total = 0
        for i in range(num_rows):
            for j in range(num_cols):
                if grid[i][j] == "1":
                    _travel_island(i, j)
                    total += 1
        
        return total
