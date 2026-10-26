class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows = len(matrix)
        cols = len(matrix[0])

        firstRowZero = any(matrix[0][c] == 0 for c in range(cols))
        firstColZero = any(matrix[r][0] == 0 for r in range(rows))

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        
        if firstRowZero:
            for c in range(cols):
                matrix[0][c] = 0

        if firstColZero:
            for r in range(rows):
                matrix[r][0] = 0
                
                            
                
        