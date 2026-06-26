class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            int remainder = target - nums[i];

            for (int j = 0; j < nums.length; j++) {
                if (i != j && nums[j] == remainder) {
                    return new int[]{i, j};
                }
            }
        }
        
        return new int[]{-1, -1};
    }
}
