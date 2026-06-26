class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> frequencyMap = new HashMap<>();

        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> Integer.compare(a[1], b[1]));

        for (int num : nums) {
            int frequency = frequencyMap.getOrDefault(num, 0) + 1;
            frequencyMap.put(num, frequency);
        }

        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            minHeap.offer(new int[]{entry.getKey(), entry.getValue()});

            if (minHeap.size() > k) minHeap.poll();
        }

        return minHeap.stream().mapToInt(x -> x[0]).toArray();
    }
}
