class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Brainstorm: 
        dfs from each cell w starting char
        memoize on index of word and coords
        need visited set for non-duplicate cells

        n is cells in board, m is length of word
        O(n * m) * DFS time complexity (hopefully 1)
        Space is also O(n * m)
        """

        R, C = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
        # memo = {}
        visited = set()

        def dfs(i, r, c):
            if i == len(word): return True
            elif r == -1 or c == -1 or r == R or c == C or (r, c) in visited: return False
            elif board[r][c] != word[i]: return False
            else:
                visited.add((r, c))

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if dfs(i+1, nr, nc): return True
                
                visited.remove((r, c))

                return False


        for r in range(R):
            for c in range(C):
                if dfs(0, r, c): return True
        
        return False
