class Solution {
    private List<List<Integer>> ret;
    private List<Integer> currCombination;
    private int currSum;

    public List<List<Integer>> combinationSum(int[] nums, int target) {
        ret = new ArrayList<>();
        currCombination = new ArrayList<>();
        currSum = 0;

        dfs(nums, target, 0);

        return ret;
    }

    private void dfs(int[] nums, int target, int i) {
        if (currSum == target) ret.add(new ArrayList<Integer>(currCombination));
        else if (currSum > target || i == nums.length) return;
        else {
            currCombination.add(nums[i]);
            currSum += nums[i];
            dfs(nums, target, i);

            currCombination.remove(currCombination.size() - 1);
            currSum -= nums[i];
            dfs(nums, target, i+1);
        }
    }
}
