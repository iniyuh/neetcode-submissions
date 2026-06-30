class Solution {
    public int search(int[] nums, int target) {
        List<Integer> numList = Arrays.stream(nums).boxed().collect(Collectors.toList());
        Collections.sort(numList);
        int index = Collections.binarySearch(numList, target);

        return index >= 0 ? index : -1;
    }
}
