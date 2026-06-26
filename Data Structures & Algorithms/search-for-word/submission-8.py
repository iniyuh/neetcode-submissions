class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        visited = set()

        def search(i, r, c):
            if r == -1 or c == -1 or r == R or c == C or (r, c) in visited: return
            elif word[i] == board[r][c]:
                if i == len(word) - 1: return True
                else:
                    visited.add((r, c))
                    for dr, dc in directions:
                        if search(i + 1, r+dr, c+dc): return True
                    visited.remove((r, c))
            
        for r in range(R):
            for c in range(C):
                if search(0, r, c): return True
        
        return False

