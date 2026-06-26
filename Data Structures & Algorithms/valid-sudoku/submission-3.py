class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def valid(vals):
            set_ = set()
            for num in vals:
                if num != '.':
                    if num in set_: return False
                    set_.add(num)
            return True
        
        for i in range(9):
            # Row
            if not valid(board[i]): return False

            # Column
            col = [board[j][i] for j in range(9)]
            if not valid(col): return False

            # Block
            r, c = (i // 3) * 3, (i % 3) * 3
            block = []
            for x in range(3): block.append(board[r][c+x])
            for x in range(3): block.append(board[r+1][c+x])
            for x in range(3): block.append(board[r+2][c+x])
            if not valid(block): return False
        
        return True