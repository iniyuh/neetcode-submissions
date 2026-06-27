class Solution {
    public int[] productExceptSelf(int[] nums) {
        int L = nums.length;

        int[] ret = new int[L];
        int[] prefix = new int[L];
        int[] suffix = new int[L];

        prefix[0] = 1;
        suffix[L-1] = 1;

        for (int i = 1; i < L; i++) {
            prefix[i] = prefix[i-1] * nums[i-1];
        }

        for (int i = L - 2; i >= 0; i--) {
            suffix[i] = suffix[i+1] * nums[i+1];
        }

        for (int i = 0; i < L; i++) {
            ret[i] = prefix[i] * suffix[i];
        }

        return ret;
    }
}  
