class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> masterSet = new HashSet<>(Set.of('1', '2', '3', '4', '5', '6', '7', '8', '9'));

        for (int i = 0; i < 9; i++) {
            Set<Character> rowSet = new HashSet<>(masterSet);
            Set<Character> colSet = new HashSet<>(masterSet);

            for (int j = 0; j < 9; j++) {
                char rowVal = board[i][j];
                if (rowVal != '.') {
                    if (rowSet.contains(rowVal)) rowSet.remove(rowVal);
                    else {
                        System.out.println("Row " + i + " error on coords [" + i + ", " + j + "]");
                        return false;
                    }
                }

                char colVal = board[j][i];
                if (colVal != '.') {
                    if (colSet.contains(colVal)) colSet.remove(colVal);
                    else {
                        System.out.println("Column " + i + " error on coords [" + j + ", " + i + "]");
                        return false;
                    }
                }
            }

            Set<Character> squareSet = new HashSet<>(masterSet);
            int r = (i / 3) * 3;
            int c = (i % 3) * 3;

            for (int dr = 0; dr < 3; dr++) {
                for (int dc = 0; dc < 3; dc++) {
                    char squareVal = board[r+dr][c+dc];

                    if (squareVal == '.') continue;
                    else if (squareSet.contains(squareVal)) squareSet.remove(squareVal);
                    else {
                        System.out.println("Square " + i + " error on coords [" + r+dr + ", " + c+dc + "]");
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
