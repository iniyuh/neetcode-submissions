class KthLargest {
    private PriorityQueue<Integer> minHeap;
    private int capacity;

    private void addToHeap(int num) {
        minHeap.offer(num);

        if (minHeap.size() > capacity) minHeap.poll();
    }

    public KthLargest(int k, int[] nums) {
        minHeap = new PriorityQueue<>();
        capacity = k;

        for (int num : nums) addToHeap(num);
    }
    
    public int add(int val) {
        addToHeap(val);
        return minHeap.peek();
    }
}
