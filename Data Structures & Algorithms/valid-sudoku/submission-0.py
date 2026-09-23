class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                if board[i][j] != '.':
                    s.add(board[i][j])
            
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                if board[j][i] != '.':
                    s.add(board[j][i])
        
        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6)
        ]
        
        for start in starts:
            s = set()

            for i in range(start[0], start[0]+3):
                for j in range(start[1], start[1]+3):
                    square = board[i][j]
                    if square in s:
                        return False
                    if square != '.':
                        s.add(square)
        
        return True