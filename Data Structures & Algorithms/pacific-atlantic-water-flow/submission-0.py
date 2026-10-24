class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(q, s):
            while q:
                cur = q.popleft()
                for dr, dc in directions:
                    nr, nc = cur[0] + dr, cur[1] + dc
                
                    if nr >= 0 and nr < len(heights) and nc >= 0 and nc < len(heights[0]):
                        if (nr, nc) not in s:
                            if heights[nr][nc] >= heights[cur[0]][cur[1]]:
                                s.add((nr, nc))
                                q.append((nr, nc))

        pq = deque()
        for col in range(len(heights[0])):
            pq.append((0, col))
            pacific.add((0, col))
        for row in range(len(heights)):
            pq.append((row, 0))
            pacific.add((row, 0))

        bfs(pq, pacific)
        
                
        # BFS on every atlantic touching cell
        aq = deque()
        for col in range(len(heights[-1])):
            aq.append((len(heights)-1, col))
            atlantic.add((len(heights)-1, col))
        for row in range(len(heights)):
            lastCol = len(heights[0]) - 1
            aq.append((row, lastCol))
            atlantic.add((row, lastCol))
        
        bfs(aq, atlantic)

        return [[r, c] for r, c in pacific & atlantic]

            
        

        