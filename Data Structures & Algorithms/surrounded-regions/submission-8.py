class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = set()

        def dfs(r, c):
            if r == -1 or c == -1 or r == R or c == C or (r, c) in visited or board[r][c] == "X": return 
            else:
                board[r][c] = "M"
                visited.add((r, c))

                for dr, dc in directions:
                    dfs(r+dr, c+dc)



        for c in range(0, C):
            for r in (0, R - 1):
                dfs(r, c)
        
        for r in range(1, R - 1):
            for c in (0, C - 1):
                dfs(r, c)
        
        for r in range(0, R):
            for c in range(0, C):
                if board[r][c] == "O": board[r][c] = "X"
                elif board[r][c] == "M": board[r][c] = "O"
        
        return

