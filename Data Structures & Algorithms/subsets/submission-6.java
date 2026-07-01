class Solution {
    List<List<Integer>> ret;
    List<Integer> currSet;

    public List<List<Integer>> subsets(int[] nums) {
        ret = new ArrayList<>();
        currSet = new ArrayList<>();

        dfs(nums, 0);
        return ret;
    }

    private void dfs(int[] nums, int i) {
        if (i == nums.length) ret.add(new ArrayList<>(currSet));
        else {
            currSet.add(nums[i]);
            dfs(nums, i+1);

            currSet.remove(currSet.size() - 1);
            dfs(nums, i+1);
        }
    }
}
