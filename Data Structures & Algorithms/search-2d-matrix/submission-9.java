class Solution {

    public boolean searchMatrix(int[][] matrix, int target) {
        int R = matrix.length, C = matrix[0].length, N = R*C;

        int l = 0, r = N;

        while (l < r) {
            int m = l + (r - l) / 2;
            int val = matrix[m / C][m % C];
            
            if (val == target) return true;
            else if (target < val) r = m;
            else l = m + 1;
        }

        return false;
    }
}
