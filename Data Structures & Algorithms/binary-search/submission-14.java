class Solution {
    public int search(int[] nums, int target) {
        Arrays.sort(nums);

        int l = 0, r = nums.length;

        while (l < r) {
            int m = l + (r - l) / 2;

            if (nums[m] == target) return m;
            else if (target < nums[m]) r = m;
            else l = m + 1;
        }

        return -1;
    }
}
