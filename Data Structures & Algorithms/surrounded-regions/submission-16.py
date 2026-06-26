class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def exploreAndMark(r, c):
            if r == -1 or c == -1 or r == R or c == C or board[r][c] != 'O': return
            else:
                board[r][c] = 'Z'
                for dr, dc in directions:
                    exploreAndMark(r+dr, c+dc)

        for r in range(R):
            exploreAndMark(r, 0)
            exploreAndMark(r, C-1)
        for c in range(C):
            exploreAndMark(0, c)
            exploreAndMark(R-1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O': board[r][c] = 'X'
                elif board[r][c] == 'Z': board[r][c] = 'O'

        return 
