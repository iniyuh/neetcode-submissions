class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # we know that if a O is on the border, it will never become
        # an x. we also know that ALL Os "connected" to said O will
        # never become Xs
        # therefore, we should dfs from all border Os for connected
        # Os and mark them all (let's say by switching them to T)
        # after this is done, we can then safely change all REMAINING
        # Os to Xs as they are not connected to any no-gos and therefore
        # CAN/WILL become Xs
        # we then change all our Ts back to Os and return

        R, C = len(board), len(board[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def dfs(r, c):
            if(
                r == -1 or
                r == R or
                c == -1 or 
                c == C or
                board[r][c] == 'X' or 
                board[r][c] == 'T'
            ): return

            board[r][c] = 'T'

            for dr, dc in directions:
                dfs(r+dr, c+dc)
        
        for r in range(R):
            dfs(r, 0)
            dfs(r, C - 1)
        
        for c in range(C):
            dfs(0, c)
            dfs(R - 1, c)

        # print(board)
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O': board[r][c] = 'X'
                elif board[r][c] == 'T': board[r][c] = 'O'