class Solution {
    private int[][] directions = new int[][]{{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    private int R;
    private int C;

    private void propagate(char[][] grid, int r, int c) {
        if (0 <= r && r < R && 0 <= c && c < C && grid[r][c] == '1') {
            grid[r][c] = '0';

            for (int[] direction : directions) {
                int dr = direction[0], dc = direction[1];

                propagate(grid, r+dr, c+dc);
            }
        }
    }

    public int numIslands(char[][] grid) {
        R = grid.length;
        C = grid[0].length;
        int islandCount = 0;

        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++) {
                if (grid[r][c] == '1') {
                    islandCount++;
                    propagate(grid, r, c);
                }
            }
        }

        return islandCount;
    }
}
