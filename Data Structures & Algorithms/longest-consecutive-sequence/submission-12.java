class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        
        int maxLength = 1;
        Map<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int val = nums[i];
            int length = 1 + hm.getOrDefault(val - 1, 0);
            hm.put(val, length);
        }

        for (Map.Entry<Integer, Integer> x : hm.entrySet()) {
            Integer target = x.getKey(), length = x.getValue();
            
            target -= length;
            while (hm.containsKey(target)) {
                length += hm.get(target);
                target -= hm.get(target);
            }

            maxLength = Math.max(maxLength, length);
        }

        return maxLength;
    }
}
