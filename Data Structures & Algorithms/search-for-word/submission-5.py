class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        W, R, C = len(word), len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()

        def dfs(letterIdx, r, c):
            if r == -1 or r == R or c == -1 or c == C: return False
            if board[r][c] == word[letterIdx]:
                print("Match ", word[letterIdx], "with", r, c)
                letterIdx += 1
                if letterIdx == W: 
                    return True
                else:
                    visited.add((r, c))
                    for dr, dc in directions:
                        if (r+dr, c+dc) not in visited and dfs(letterIdx, r+dr, c+dc): return True
                    visited.remove((r, c))

                    return False

            else: return False
        
        for r in range(R):
            for c in range(C):
                if dfs(0, r, c): return True
        
        return False
        
