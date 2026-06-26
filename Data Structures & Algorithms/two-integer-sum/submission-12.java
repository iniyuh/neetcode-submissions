class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> valueToIndex = new HashMap<>();

        for (Integer i = 0; i < nums.length; i++) {
            Integer remainder = target - nums[i];

            if (valueToIndex.containsKey(remainder)) {
                return new int[]{valueToIndex.get(remainder), i};
            }

            valueToIndex.put(nums[i], i);
        }

        return new int[]{-1, -1};
    }
}
